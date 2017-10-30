import math

"""
Helps convert network packets into bytes
"""
class Depacketizer(object):

    def __init__(self, num_packets, final_packet_size, packet_size=1024):
        self.packets_remaining = num_packets
        self.final_packet_size = final_packet_size
        self.packet_size = packet_size
        self.data = b""

    """
    The size of each packet
    """
    def PacketSize(self):
        return self.packet_size

    """
    The number of expected packets left to depacketize
    """
    def PacketsRemaining(self):
        return self.packets_remaining

    """
    The size of the final offset packet
    """
    def FinalPacketSize(self):
        return self.final_packet_size

    """
    Whether or not the depacketizer is expecting the final packet
    """
    def OnFinalPacket(self):
        return self.packets_remaining == 1

    """
    Whether or not the depacketizer has finished packetizing
    """
    def Done(self):
        return self.packets_remaining <= 0

    """
    Takes a packet and advances the depacketizer
    """
    def Next(self, data):
        if self.Done():
            raise ValueError('Expected number of packets has been reached')
        if self.OnFinalPacket():
            data = self.RemoveZeroPadding(data, self.packet_size-self.final_packet_size)
        self.data += data
        self.packets_remaining -= 1

    """
    The collected depacketized data so far
    """
    def Data(self):
        return self.data

    """
    Removes right-size zero padding of null bytes
    """
    def RemoveZeroPadding(self, data, padding_size):
        return data[:len(data)-padding_size]
