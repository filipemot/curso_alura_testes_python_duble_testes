from unittest import skip
from unittest.mock import patch, mock_open, Mock
from urllib.error import HTTPError

import pytest
from sympy import Dummy

from colecao.livros import consultar_livros, executar_requisicao


@skip("Vale quando consultar livros estiver completo")
def test_consultar_livros_retorna_resultado_formato_string():
    resultado = consultar_livros("Agatha Christie")
    assert type(resultado) == str

@skip("")
def test_consultar_livros_chama_preparar_dados_para_requisicao_uma_vez_e_com_os_mesmos_parametros_de_consultar_livros():
    with patch("colecao.livros.preparar_dados_para_requisicao") as duble:
        consultar_livros("Agatha Christie")
        duble.assert_called_once_with("Agatha Christie")

@skip("")
def test_consultar_livros_chama_obter_url_usando_como_parametro_o_retorno_de_preparar_dados_para_requisicao():
    with patch("colecao.livros.preparar_dados_para_requisicao") as duble_preparar_dados_para_requisicao:
        dados = {"author": "Agatha Christie"}
        duble_preparar_dados_para_requisicao.return_value = dados
        with patch("colecao.livros.obter_url") as duble_obter_url:
            consultar_livros("Agatha Christie")
            duble_obter_url.assert_called_once_with("http://buscador", dados)

def test_consultar_livros_chama_executar_requisicao_usando_retorno_obter_url():
    with patch("colecao.livros.obter_url") as duble_obter_url:
        duble_obter_url.return_value = "http://buscador"
        with patch("colecao.livros.executar_requisicao") as duble_executar_requisicao:
            consultar_livros("Agatha Christie")
            duble_executar_requisicao.assert_called_once_with("http://buscador")

class StubHTTPResponse:
    def read(self):
        return b""
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
"""
def duble_urlopen(url, timeout):
    return StubHTTPResponse()

def test_executar_requisicao_retorna_tipo_string():
    with patch("colecao.livros.urlopen", duble_urlopen):
        resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")

    assert type(resultado) == str

def test_executar_requisicao_retorna_tipo_string():
    with patch("colecao.livros.urlopen") as duble_urlopen:
        duble_urlopen.return_value = StubHTTPResponse()
        resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")

    assert type(resultado) == str

def test_executar_requisicao_retorna_tipo_string():
    with patch("colecao.livros.urlopen", return_value=StubHTTPResponse()):
        resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")

    assert type(resultado) == str

@patch("colecao.livros.urlopen", return_value=StubHTTPResponse())
def test_executar_requisicao_retorna_tipo_string(duble_url_open):
    resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")

    assert type(resultado) == str
"""
@patch("colecao.livros.urlopen")
def test_executar_requisicao_retorna_tipo_string(duble_url_open):
    duble_url_open.return_value = StubHTTPResponse()
    resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")

    assert type(resultado) == str

def duble_urlopen_error(url, timeout):
    fp = mock_open()
    fp.close = Dummy()
    raise HTTPError(Dummy(), Dummy(), "mensagem_error", Dummy(), fp)

def test_executar_requisicao_levanta_excecao_http_error():
    with patch("colecao.livros.urlopen", duble_urlopen_error):
        with pytest.raises(HTTPError) as excecao:
            resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")

        assert "mensagem_error" in str(excecao)



@patch("colecao.livros.urlopen")
def test_executar_requisicao_levanta_excecao_http_error_unittest_mock(duble_urlopen):
    fp = mock_open()
    fp.close = Mock()
    duble_urlopen.side_effect = HTTPError(Mock(), Mock(), "mensagem_error", Mock(), fp)
    with pytest.raises(HTTPError) as excecao:
        resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")
    assert "mensagem_error" in str(excecao.value)

def stub_urlopen_error(url, timeout):
    fp = mock_open()
    fp.close = Dummy()
    raise HTTPError(Dummy(), Dummy(), "mensagem de erro", Dummy(), fp)

def test_executar_requisicao_loga_mensagem_erro_httop_error(caplog):
    with patch("colecao.livros.urlopen", stub_urlopen_error):
        message_error = "mensagem de erro"
        resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")
        assert len(caplog.records) == 1
        for registro in caplog.records:
            assert message_error in registro.message


@patch("colecao.livros.urlopen")
def test_executar_requisicao_loga_mensagem_erro_httop_error_mock(duble_url_open, caplog):
    fp = mock_open()
    fp.close = Mock()
    duble_url_open.side_effect = HTTPError(Mock(), Mock(), "mensagem de erro", Mock(), fp)

    message_error = "mensagem de erro"
    resultado = executar_requisicao("https://buscarlivros?author=Jk+Rowlings")
    assert len(caplog.records) == 1
    for registro in caplog.records:
        assert message_error in registro.message