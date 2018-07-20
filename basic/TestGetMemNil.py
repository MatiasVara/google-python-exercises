#!/usr/bin/python -tt
import sys

def checkgetmemnil(file):
  f = open (file, 'rU')
  nrline = 0
  result = 0
  while 1 :
      line = f.readline()
      lastline = f.tell()
      nrline += 1
      if not line : break
      line.lstrip()
      i = line.find(':= ToroGetMem')
      if not i == -1:
          var = line[:i].lstrip()
          line = f.readline()
          line = f.readline()
          nrline += 2
          if not line: break
          # we expect something like if var = nil
          line.lstrip()
          i = line.find('if ' +  var + "= nil")
          if i == -1:
              print "Warning(line:" + str(nrline)+ "): Variable " + var + "is not checked"
              f.seek(lastline)
              result = 1
  f.close()
  return result

def main():
    if checkgetmemnil('Network.pas') == 0:
        print "checkgetmemnil: OK"
    else:
        print "checkgetmemnil: KO"

if __name__ == '__main__':
  main()
