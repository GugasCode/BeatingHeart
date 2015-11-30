import wave
import struct
import numpy as np

def __openWave(path):
    return wave.open(path, 'rb')

def __closeWave(wav):
    wav.close()

def loadWave(path)
    wav = __openWave(path)
    values = {
            'nchannels' : wav.getnchannels(),
            'nframes' : wav.getnframes(),
            'framerate' : wav.getframerate(),
            'samplewidth' : wav.getsampwidth(),
            'frames' : wave.readframes(wav.getnframes())
            }
    __closeWave(wav)
    return values

@loadWave
def getSamples(values):
    """ Generates an array containing the amplitude of each frame """
    # Total number of bytes

    size = values.get('nframes') * values.get('nchannels')
        * values.get('samplewidth') + 1
    value = values.get('frames')
    result = np.array([], np.int32)

    # Mono channel
    if values.get('nchannels') == 1:
        # 16 bits data
        if value.get('samplewidth') == 2:
            for i in range(2, size, 2):
                # read two bytes of information, in little endian
                res = struct.unpack('<h', value[i-2:i])[0]
                result = np.append(result, res)
        # 8 bits data
        elif value.get('samplewidth') == 1:
            for i in range(1, size):
                res = struct.unpack('<c', value[i-1:i])[0]
                result = np.append(result, res)
    # Stereo channel
    else:
        # 16 bits data
        if value.get('samplewidth') == 2:
            for i in range(4, size, 8):
                res1 = struct.unpack('<i', value[i-4:i])[0]
                res2 = struct.unpack('<i', value[i:i+4])[0]
                res = (res1 + res2) // 2
                result = np.append(result, res)
        # 8 bits data
        if value.get('samplewidth') == 1:
            for i in range(2, size, 4):
                res1 = struct.unpack('<i', value[i-2:i])[0]
                res2 = struct.unpack('<i', value[i:i+2])[0]
                res = (res1 + res2) // 2
                result = np.append(result, res)

    return np.append([result], [np.array(range(size))], axis=0)
