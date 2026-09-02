"""
Simulação Oficial: Usuário / Agente Externo Consumindo a API do CV Maker 2.0
=============================================================================
Demonstração do fluxo Agent-Native & YAML-First:
1. Auto-provisionamento de Chave Efêmera via API
2. Envio de dados estruturados com autenticação Authorization: Bearer <token>
3. Obtenção de YAML validado e dados estruturados da API
"""

import os
import sys
import requests

# Forçar stdout em UTF-8 para terminais Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ── Configurações de Conexão ─────────────────────────────────────────────────
API_URL = os.getenv("CV_API_URL", "http://127.0.0.1:8000")


def obter_chave():
    print("[1/3] Solicitando Chave Temporária via API...")
    try:
        res = requests.post(f"{API_URL}/api/v1/api-keys/generate", json={"ttlDays": 1}, timeout=10)
        if res.status_code == 200:
            key = res.json().get("apiKey")
            print(f"      Chave provisionada com sucesso: {key[:14]}...{key[-6:]}")
            return key
    except Exception as e:
        print(f"      Aviso: Falha ao conectar em {API_URL}: {e}")
    return "am_sheet_live_fallback_chave"


API_KEY = obter_chave()

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",  # Padrão Primário Unificado
}

YAML_FILE = os.path.join(os.path.dirname(__file__), "cv-ptbr.yaml")
OUTPUT_YAML = os.path.join(os.path.dirname(__file__), "meu_curriculo_via_api.yaml")


def main():
    print("=" * 65)
    print("SIMULACAO DO CLIENTE EXTERNO - CV MAKER 2.0 (YAML-FIRST)")
    print("=" * 65)
    print(f"Servidor: {API_URL}")
    print(f"Header de Autenticação: Authorization: Bearer {API_KEY[:14]}...\n")

    # 1. Carrega o YAML local
    if os.path.exists(YAML_FILE):
        with open(YAML_FILE, "r", encoding="utf-8") as f:
            yaml_content = f.read()
    else:
        yaml_content = "basics:\n  name: Demo\n  label: AI Engineer\n"

    print(f"[2/3] Enviando {len(yaml_content)} caracteres de YAML para validação e compilação...")

    # 2. Chamada HTTP com format="yaml"
    response = requests.post(
        f"{API_URL}/api/v1/cv/render",
        headers=HEADERS,
        json={
            "raw_text": yaml_content,
            "theme": "executive",
            "format": "yaml"
        },
        timeout=30
    )

    if response.status_code != 200:
        print(f"Erro na API ({response.status_code}): {response.text}")
        return

    yaml_recebido = response.text
    print(f"      Sucesso! O servidor retornou {len(yaml_recebido)} bytes de YAML estruturado.")

    # 3. Salva o YAML retornado em disco
    print(f"[3/3] Salvando arquivo YAML em disco...")
    with open(OUTPUT_YAML, "w", encoding="utf-8") as f:
        f.write(yaml_recebido)

    print(f"      Arquivo salvo com sucesso em: {OUTPUT_YAML}")
    print("\n" + "=" * 65)
    print("RESUMO DO PROCESSO:")
    print("1. O agente/usuário enviou dados autenticados via Bearer token.")
    print("2. A API validou e processou os dados de forma pura (YAML-Only).")
    print("3. A renderização visual para visualização/PDF é compilada no frontend.")
    print("=" * 65)


if __name__ == "__main__":
    main()
