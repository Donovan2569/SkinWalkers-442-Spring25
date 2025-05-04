import sys

SENTINEL = bytes([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

def store_byte(wrapper, hidden, offset, interval):
    for byte in hidden + SENTINEL:
        wrapper[offset] = byte
        offset += interval
    return wrapper

def store_bit(wrapper, hidden, offset, interval):
    for byte in hidden + SENTINEL:
        for bit in range(8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= (byte >> (7 - bit)) & 1
            offset += interval
    print("Sentinel embedded at byte offset:", offset, file=sys.stderr)
    return wrapper

def retrieve_byte(wrapper, offset, interval):
    result = bytearray()
    while offset < len(wrapper):
        result.append(wrapper[offset])
        if len(result) >= len(SENTINEL) and result[-len(SENTINEL):] == SENTINEL:
            return result[:-len(SENTINEL)]
        offset += interval
    return result

def retrieve_bit(wrapper, offset, interval):
    result = bytearray()
    byte = 0
    while offset < len(wrapper):
        for bit in range(8):
            byte = (byte << 1) | (wrapper[offset] & 1)
            offset += interval
        result.append(byte)
        byte = 0
        if len(result) >= len(SENTINEL) and result[-len(SENTINEL):] == SENTINEL:
            return result[:-len(SENTINEL)]
    return result

def parse_args(args):
    opts = {
        'mode': None,
        'method': None,
        'offset': 0,
        'interval': 1,
        'wrapper': None,
        'hidden': None
    }
    for arg in args:
        if arg == '-s':
            opts['mode'] = 'store'
        elif arg == '-r':
            opts['mode'] = 'retrieve'
        elif arg == '-b':
            opts['method'] = 'bit'
        elif arg == '-B':
            opts['method'] = 'byte'
        elif arg.startswith('-o'):
            opts['offset'] = int(arg[2:])
        elif arg.startswith('-i'):
            opts['interval'] = int(arg[2:])
        elif arg.startswith('-w'):
            opts['wrapper'] = arg[2:]
        elif arg.startswith('-h'):
            opts['hidden'] = arg[2:]
    return opts

def main():
    opts = parse_args(sys.argv[1:])

    if not opts['mode'] or not opts['method'] or not opts['wrapper']:
        print(f"Usage: python {sys.argv[0]} -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
        return

    with open(opts['wrapper'], 'rb') as f:
        wrapper = bytearray(f.read())

    if opts['mode'] == 'store':
        if not opts['hidden']:
            print("Error: Hidden file required for store mode.", file=sys.stderr)
            return
        with open(opts['hidden'], 'rb') as f:
            hidden = f.read()
        if opts['method'] == 'bit':
            wrapper = store_bit(wrapper, hidden, opts['offset'], opts['interval'])
        else:
            wrapper = store_byte(wrapper, hidden, opts['offset'], opts['interval'])
        with open("wrapped_output.bmp", "wb") as f:
            f.write(wrapper)
        print("Stego image saved as wrapped_output.bmp")

    elif opts['mode'] == 'retrieve':
        if opts['method'] == 'bit':
            hidden = retrieve_bit(wrapper, opts['offset'], opts['interval'])
        else:
            hidden = retrieve_byte(wrapper, opts['offset'], opts['interval'])
        with open("extracted_output.txt", "wb") as f:
            f.write(hidden)
        print("Hidden data written to extracted_output.txt")

if __name__ == "__main__":
    main()
