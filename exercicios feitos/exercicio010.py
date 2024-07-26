m = int(input('digite a quantidade de metros para eu te dar em varias medidas:'))
cm = m * 100
mm = m * 1000
km = m / 1000
dc = m / 10
hc = m / 100
print('a quantidade de {} metros.\nEm centimetros e de: {}.\nEm milimetros e de: {}.\nEm decametros e de: {}\nEm hectometros e de: {}.\nE em kilometros e de: {}.'.format(m,cm,mm,dc,hc,km))
