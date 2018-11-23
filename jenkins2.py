import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='admin1', password='admin1')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))