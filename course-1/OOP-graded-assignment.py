#In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.

#To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server. For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections"""
        self.connections = {}

    def add_connections(self, connection_id):
        """Adds a new connection to this server"""
        connection_load = random.random()*10 + 1
        self.connections[connection_id] = connection_load
        # add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        """closes a connection to this server"""
        #remove the connection from this server
        if connection_id != None:
            del self.connections[connection_id]


    def load(self):
        """calculates the current load for all connections"""
        total = 0 
        for user in self.connections:
            total += self.connections[user]
        return total

    def __str__(self):
        """returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

server = Server()
server.add_connections("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

#LoadBalancing class

class LoadBalancing:
    def __init__(self):
        """initialize the load balancing system with one server"""
        self.connections = {}
        self.servers =[Server()]


    def add_connection(self, connection_id):
        """randomly selects a server and adds a connection ot it"""
        server = random.choice(self.servers)
        # add the connection to the dictionary with the selected server
        # add the connection to the server
        self.connections[connection_id] = server
        server.add_connections(connection_id)
        self.ensure_availability()
                
    def close_connection(self, connection_id):
        """Closes the connection t=on the server corresponding to connection_id"""
        # find out the right server
        # close the connection on the server
        # remove the connection from the load balancer
        for connection in self.connections.keys():
            if connection == connection_id:
                server_of_connection = self.connections[connection]

        server_of_connection.close_connection(connection_id)
        del self.connections[connection_id]

        
    def avg_load(self):
        """Calculates the average load of all servers"""
        result = 0
        loads = 0
        for server in self.servers:
            result += server.load()
            loads += 1
        return result/loads

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() >= 50:
            self.servers.append(Server())
            
    def __str__(self) -> str:
        """returns a sring with a load for each server"""

        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

l = LoadBalancing()
l.add_connection("fdca:83d2:f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2:f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())