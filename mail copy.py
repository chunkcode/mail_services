from O365 import Message , MSGraphProtocol
protocol = MSGraphProtocol()
o365_auth = ('techsupport@gisfy.co.in','Gisfy@1&%')
m = Message(auth=o365_auth, protocol=protocol)
m.to.add('ram@gisfy.co.in')
m.body = 'Hi, foobar.'
m.subject = 'Bar Foo'
m.send()