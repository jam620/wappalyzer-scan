#!/usr/local/bin/python3
# _*_ coding: utf8 _*_

from Wappalyzer import Wappalyzer, WebPage


def main():
    wappalyzer = Wappalyzer.latest()
    try:
        web = WebPage.new_from_url("http://morenojose.com")
        techs = wappalyzer.analyze(web)
        # no funciona
        '''for tech in techs:
            print("Tecnología detectada: {}".format(tech))'''
        print("Tecnología detectada: {}".format(techs))

    except:
        print("[-] Ha ocurrido un error")


if __name__ == 'main':
    try:
        main()
    except KeyboardInterrupt:
        print("[-] Saliendo")
        exit()
