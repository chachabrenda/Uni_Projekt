#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
import argparse
from mininet.link import TCLink  # Importiere den TCLink-Typ

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


class  ParkingLotTopo( Topo ):
    "A LinuxRouter connecting three IP subnets"

    # pylint: disable=arguments-differ
    def build( self, **_opts ):

     # Create sender hosts and routers
        senders = []
        routers = []
        for i in range(1,n+1):
             router = self.addNode( f'r{i}', cls=LinuxRouter, ip = None)
             routers.append(router)

        # Verbindung zwischen den Routern erstellen
        for i in range(1,n):
          routerip = '10.0.' + str(i) + '.1' + '/8'
          routerip2 = '10.0.' + str(i) + '.2' + '/8'
          self.addLink( routers[i-1], routers[i], intfName1=routers[i-1] + '-eth' + str(i),
                                                  intfName2=routers[i] + '-eth' + str(i),
                                                  params1={ 'ip' : routerip },
                                                  params2={ 'ip' : routerip2 },
                                                  cls=TCLink, bw=maxrate)

       # Verbindung des Empfängerhosts mit dem ersten Router herstellen
        recv = self.addHost('recv', ip = '10.0.0.1/8', defaultRoute='via 10.0.0.2')
        self.addLink( recv, routers[0], intfName1='recv-eth0', intfName2='r1-eth0',
                      params1={ 'ip' : '10.0.0.1/8' },
                      params2={ 'ip' : '10.0.0.2/8'} )

       # Verbindung der Senderhosts mit den Routern herstellen
        for i in range(1,n+1):
           host = 'h' + str(i)
           host_ip = '{}.{}.{}.{}/8'.format(i, i, i, i)
           host_defaultroute= 'via {}.{}.{}.254'.format(i, i, i)
           sender = self.addHost(host, ip = host_ip, defaultRoute = host_defaultroute)
           senders.append(sender)

           routerintf = routers[i-1] + '-eth' + str(i) + str(i)
           hostintf = senders[i-1] + '-eth' + str(i) + str(i)
           routerip = str(i) + '.'+ str(i)+'.'+ str(i) + '.'+ '254' + '/8'
           routerip2 = str(i) + '.' + str(i) + '.'+ str(i) + '.'+ str(i) + '/8'
           self.addLink( routers[i-1], senders[i-1], intfName1=routerintf, intfName2=hostintf,
                      params1={ 'ip' : routerip },
                      params2={ 'ip' : routerip2 },
                      cls=TCLink, bw=maxrate)


def run():
    "Test linux router"
    topo = ParkingLotTopo()
    net = Mininet( topo=topo,
                   waitConnected=True )  
    net.start()

    # routing all router to the right side
    for i in range(1,n+1):
        for j in range(1,n):
            if(j < i):
                routeadd = 'ip route add ' + '10.0.' + str(j) + '.2'
                via = ' via ' + '10.0.' + str(i-1) + '.1'
                dev = ' dev ' 'r' + str(i) + '-eth' + str(i-1)
                info(net['r'+ str(i)].cmd(routeadd + via + dev))
            elif (j >= i):
                routeadd = 'ip route add ' + '10.0.' + str(j) + '.2'
                via = ' via ' + '10.0.' + str(i) + '.2'
                dev = ' dev ' 'r' + str(i) + '-eth' + str(i)
                info(net['r'+ str(i)].cmd(routeadd + via + dev))

    # routing all router to the left side
    for i in range(n,1,-1):
        for j in range(n,1,-1):
            routeadd = 'ip route add ' + '10.0.' + str(j-1) + '.1'
            via = ' via ' + '10.0.' + str(i-1) + '.1'
            dev = ' dev ' 'r' + str(i) + '-eth' + str(i-1)
            info(net['r'+ str(i)].cmd(routeadd + via + dev))

    #  routing recv to all router"#

    info(net['recv'].cmd('ip route add 10.0.0.2 via 10.0.0.2 dev recv-eth0'))
    for i in range(1,n+1):
            routeadd = 'ip route add ' + '10.0.' + str(i) + '.2'
            via = ' via ' + '10.0.0.2'
            dev = ' dev ' 'recv-eth0'
            info(net['recv'].cmd(routeadd + via + dev))

   #routing all router to recv"#
    for i in range(n,0,-1):
        routeadd = 'ip route add ' + '10.0.0.1'
        via = ' via ' + '10.0.' + str(i-1) + '.1'
        dev = ' dev ' 'r' + str(i) + '-eth' + str(i-1)
        info(net['r'+ str(i)].cmd(routeadd + via + dev))

   # routing hosts to router"#
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(j < i):
                routeadd = 'ip route add ' + str(i) + '.' + str(i)+'.' + str(i)+'.'+ str(i)
                via = ' via ' + '10.0.' + str(j) + '.2'
                dev = ' dev ' 'r' + str(j) + '-eth' + str(j)
                info(net['r'+ str(j)].cmd(routeadd + via + dev))
            elif(j > i):
                routeadd = 'ip route add ' + str(i) + '.' + str(i)+'.'+ str(i)+'.'+ str(i)
                via = ' via ' + '10.0.' + str(j-1) + '.1'
                dev = ' dev ' 'r' + str(j) + '-eth' + str(j-1)
                info(net['r'+ str(j)].cmd(routeadd + via + dev))
            else:
                continue


    # routing router to hosts
    for i in range(1,n+1):
        for j in range(1,11):
            if(j < i):
                routeadd = 'ip route add ' + '10.0.' + str(j) + '.1'
                via = ' via ' + str(i) + '.' + str(i)+'.'+ str(i) + '.254'
                dev = ' dev ' + 'h' + str(i) + '-eth' + str(i)+ str(i)
                info(net['h'+ str(i)].cmd(routeadd + via + dev))

    if (n == 10):
        for i in range(1,n-1):
            routeadd = 'ip route add ' + '10.0.' + str(i) + '.2'
            via = ' via 10.10.10.254'
            dev = ' dev h10-eth1010'
            info(net['h10'].cmd( routeadd + via + dev))
           

        info(net['h10'].cmd( 'ip route add 10.0.0.1 via 10.10.10.254 dev h10-eth1010'))

        info(net['r10'].cmd( 'ip route add 10.10.10.10 via 10.10.10.10 dev r10-eth1010'))

        info(net['recv'].cmd( 'ip route add 10.10.10.10 via 10.0.0.2 dev recv-eth0'))

    info('*** Routing Table on Routers:\n')
    for i in range(1, n+1):
        router = net.get(f'r{i}')
        info(f'{router.name}:\n')
        info(router.cmd('ip route'))
        info('\n')

    info('*** Routing Table on Receiver:\n')


    CLI( net )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    parser = argparse.ArgumentParser()
    parser.add_argument('--hosts', action='store', type=int, default=5, help='add number of hosts')
    parser.add_argument('--maxrate', action='store', type=int, help='specify the maximum data rate in MBit/s')
    args = parser.parse_args()
    n = args.hosts
    maxrate = args.maxrate
    run()
