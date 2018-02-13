import xml.dom.minidom
def node_text(node):
    text = ''
    for child in node.childNodes:
        if child.nodeType is child.TEXT_NODE:
            text += child.data
        return text
        
if __name__=="__main__":
    x = xml.dom.minidom.parse('arquivos\\AndesConfiguracao.xml')
    nos = x.documentElement
    print "|-> %s" % nos.nodeName
    filhos1 = [no for no in nos.childNodes if no.nodeType == \
                  x.ELEMENT_NODE]
         
    for pai in filhos1:
        print "|--> %s" % pai.nodeName
        filhos2 = [no for no in pai.childNodes if no.nodeType == \
                      x.ELEMENT_NODE]
        for filho in filhos2:
            print "|---> %s" % filho.nodeName
            print "|-----> %s" % node_text(filho)