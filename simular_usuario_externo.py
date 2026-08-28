"""
Simulacao Oficial: Usuario Externo Consumindo a API do CV Maker
=============================================================================
Este script simula exatamente o que uma pessoa externa (ou agente de IA)
faz tendo apenas a URL da API e a Chave de API, sem nenhum codigo local de design.
"""

import os
import sys
import requests

# Forçar stdout em UTF-8 para terminais Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ── 1. As UNICAS informacoes que o usuario externo precisa: ──
API_URL = "https://ocorrencias-pdf-writer.onrender.com"

# Se o usuário não tiver chave, o script pode auto-provisionar uma na hora:
def obter_chave():
    print("[1/3] Solicitando Chave Temporaria via API...")
    res = requests.post(f"{API_URL}/api/v1/api-keys/generate", json={"ttlDays": 1})
    if res.status_code == 200:
        key = res.json().get("apiKey")
        print(f"      Chave provisionada com sucesso: {key[:14]}...{key[-6:]}")
        return key
    return "am_sheet_live_fallback_chave"

API_KEY = obter_chave()

HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY,          # Header Universal
    "X-Spreadsheet-Key": API_KEY   # Compativel com Assistente Moeda
}

YAML_FILE = os.path.join(os.path.dirname(__file__), "cv-ptbr.yaml")
OUTPUT_HTML = os.path.join(os.path.dirname(__file__), "meu_curriculo_via_api.html")

def main():
    print("=" * 65)
    print("SIMULACAO DO CLIENTE EXTERNO - CV MAKER API")
    print("=" * 65)
    print(f"Conectando ao Servidor Remoto: {API_URL}")
    print(f"Chave de Autenticacao: {API_KEY[:16]}...{API_KEY[-8:]}\n")

    # 1. Carrega o YAML local do usuário
    with open(YAML_FILE, "r", encoding="utf-8") as f:
        yaml_content = f.read()

    print(f"[2/3] Enviando {len(yaml_content)} caracteres de YAML para renderizacao remota...")

    # 2. Faz a chamada HTTP pura para a rota /render da API
    response = requests.post(
        f"{API_URL}/api/v1/cv/render",
        headers=HEADERS,
        json={
            "raw_text": yaml_content,
            "theme": "executive"  # Opcoes: executive, creative, minimalist, white, terminal
        },
        timeout=30
    )

    if response.status_code != 200:
        print(f"Erro na API ({response.status_code}): {response.text}")
        return

    # 3. O servidor devolve o HTML completo ja desenhado e estilizado!
    html_recebido = response.text
    print(f"      Sucesso! O servidor devolveu {len(html_recebido)} bytes de HTML estilizado.")

    # 4. O usuário externo apenas salva o arquivo no seu computador
    print(f"[3/3] Salvando arquivo HTML standalone em disco...")
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_recebido)

    print(f"      Arquivo salvo com sucesso em: {OUTPUT_HTML}")
    print("\n" + "=" * 65)
    print("RESUMO DO PROCESSO:")
    print("1. O usuario enviou apenas o YAML bruto para a API.")
    print("2. O servidor cuidou de TODO o CSS, fontes e regras de impressao A4.")
    print("3. O arquivo HTML recebido ja contem o botao de download / impressao em PDF!")
    print("=" * 65)

if __name__ == "__main__":
    main()
