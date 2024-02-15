#!/usr/bin/env python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

     # pylint: disable=arguments-differ
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

class NetworkTopo( Topo ):
    "A LinuxRouter connecting three IP subnets"

     # pylint: disable=arguments-differ
    def build(self, **_opts):

       # Create router nodes
         r1 = self.addNode( 'r1', cls=LinuxRouter, ip=None ,defaultRoute= 'via 192.168.56.1' )
         r2 = self.addNode( 'r2', cls=LinuxRouter, ip=None ,defaultRoute= 'via 192.168.56.2')


        # Create switch nodes
         s1 = self.addSwitch('S1')
         s2 = self.addSwitch('S2')
         s3 = self.addSwitch('S3')
         s4 = self.addSwitch('S4')

        # Connect switches to routers
         self.addLink( s1, r1, intfName2='r1-eth1', params2={ 'ip' : '192.168.0.15/24' } )  
         self.addLink( s2, r1, intfName2='r1-eth2', params2={ 'ip' : '193.168.0.16/24' } )
         self.addLink( s3, r2, intfName2='r2-eth1', params2={ 'ip' : '194.168.0.17/24' } )
         self.addLink( s4, r2, intfName2='r2-eth2', params2={ 'ip' : '195.168.0.18/24' } )
         
        
         self.addLink(r1, r2, intfName1='r1-eth3', intfName2='r2-eth3', params1={'ip': '192.168.56.2/24'}, params2={'ip': '192.168.56.1/24'})
        # Create host nodes
         h1 = self.addHost( 'h1', ip='192.168.0.1/24', defaultRoute='via 192.168.0.15' )
         h2 = self.addHost( 'h2', ip='192.168.0.2/24', defaultRoute='via 192.168.0.15' )
         h3 = self.addHost( 'h3', ip='192.168.0.3/24', defaultRoute='via 192.168.0.15' )
         h4 = self.addHost( 'h4', ip='193.168.0.4/24', defaultRoute='via 193.168.0.16' )
         h5 = self.addHost( 'h5', ip='193.168.0.5/24', defaultRoute='via 193.168.0.16' )
         h6 = self.addHost( 'h6', ip='193.168.0.6/24', defaultRoute='via 193.168.0.16' )
         h7 = self.addHost( 'h7', ip='193.168.0.7/24', defaultRoute='via 193.168.0.16' )
         h8 = self.addHost( 'h8', ip='194.168.0.8/24', defaultRoute='via 194.168.0.17' )
         h9 = self.addHost( 'h9', ip='194.168.0.9/24', defaultRoute='via 194.168.0.17' )
         h10 = self.addHost('h10',ip='194.168.0.10/24',defaultRoute='via 194.168.0.17' )
         h11 = self.addHost('h11',ip='195.168.0.11/24',defaultRoute='via 195.168.0.18' )
         h12 = self.addHost('h12',ip='195.168.0.12/24',defaultRoute='via 195.168.0.18' )
         h13 = self.addHost('h13',ip='195.168.0.13/24',defaultRoute='via 195.168.0.18' )
         h14 = self.addHost('h14',ip='195.168.0.14/24',defaultRoute='via 195.168.0.18' )


        # Connect hosts to switches
         for h, s in [(h1, s1), (h2, s1), (h3, s1), (h4, s2), (h5, s2), (h6, s2), (h7, s2),
                     (h8, s3), (h9, s3), (h10, s3), (h11, s4), (h12, s4), (h13, s4), (h14, s4)]:
            self.addLink(h, s)

def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet(topo=topo,
                  waitConnected=True )
    net.start()
    info( '*** Routing Table on Router:\n' )
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()

