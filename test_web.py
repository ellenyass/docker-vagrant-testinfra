
def test_apache_instalado(host):
    apache = host.package("apache2")
    assert apache.is_installed


def test_apache_ativo(host):
    apache = host.service("apache2")
    assert apache.is_running


def test_apache_habilitado(host):
    apache = host.service("apache2")
    assert apache.is_enabled


def test_porta_http(host):
    porta = host.socket("tcp://0.0.0.0:80")
    assert porta.is_listening


def test_pagina_inicial(host):
    pagina = host.file("/var/www/html/index.html")
    assert pagina.exists


def test_conteudo_html(host):
    pagina = host.file("/var/www/html/index.html")
    assert "Servidor Web funcionando!" in pagina.content_string
