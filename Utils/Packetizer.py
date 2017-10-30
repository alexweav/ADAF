import math

"""
Helps convert bytes into network packets
"""
class Packetizer(object):

    def __init__(self, data, packet_size=1024):
        self.data = data
        self.packet_size = packet_size
        self.final_packet_size = len(self.data) % self.packet_size
    
    """
    Size of each packet
    """
    def PacketSize(self):
        return self.packet_size
    
    """
    Number of packets remaining
    """
    def PacketsRemaining(self):
        return math.ceil(len(self.data) / self.packet_size)

    """
    Length of the final offset packet
    """
    def FinalPacketSize(self):
        return self.final_packet_size

    """
    Whether or not the packetizer is ready to send the final packet
    """
    def OnFinalPacket(self):
        return len(self.data) != 0 and len(self.data) < self.packet_size

    """
    Whether or not the packetizer is done with the data stream
    """
    def Done(self):
        return self.data is None or len(self.data) == 0

    """
    Gets the next packet from the data
    """
    def Next(self):
        if self.Done():
            raise ValueError('Packets have all already been consumed')
        if self.OnFinalPacket():
            packet = self.data
            self.data = b""
            return self.ZeroPadData(packet, self.packet_size - len(packet))
        packet = self.data[:self.packet_size]
        self.data = self.data[self.packet_size:]
        return packet

    """
    Pads a piece of data with null bytes
    """
    def ZeroPadData(self, data, pad_amount):
        return data + (b"\x00" * pad_amount)
