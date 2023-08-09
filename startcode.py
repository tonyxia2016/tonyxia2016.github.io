input_file = 'bbb_video_avc_frag.h264'
output_file = 'output.h264'

with open(input_file, 'rb') as infile:
    bytes_data = infile.read()

new_data = bytearray()
i = 0
while i < len(bytes_data):
    if (i < len(bytes_data) - 2 and
            bytes_data[i] == 0x00 and
            bytes_data[i + 1] == 0x00 and
            bytes_data[i + 2] == 0x01):
        # 检查前一个字节是否为0，如果不是，则添加额外的零字节
        if i == 0 or bytes_data[i - 1] != 0x00:
            new_data.append(0x00)
        new_data.extend(b'\x00\x00\x01')
        i += 3
    else:
        new_data.append(bytes_data[i])
        i += 1

with open(output_file, 'wb') as outfile:
    outfile.write(new_data)
