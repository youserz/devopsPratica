# Pipeline DevSecOps

O workflow `.github/workflows/ci.yml` executa em PRs para `main` e pushes na `main`.

| Ferramenta | Bloqueio |
| --- | --- |
| Gitleaks | Possíveis segredos em todo o histórico (`fetch-depth: 0`, `--all`) |
| Ruff e pytest | Erros de lint, contrato HTTP ou testes |
| SonarCloud | Quality Gate sobre código novo reprovado |
| Trivy (dependências e imagem) | HIGH/CRITICAL com correção disponível |
| Syft | Falha ao gerar ou guardar o SBOM SPDX JSON |

Trivy produz relatórios de todas as severidades antes do gate. Os manifests de
execução e desenvolvimento são preparados em diretórios separados com o nome
`requirements.txt`, reconhecido pelo scanner. Isso inclui as dependências transitivas
fixadas e evita deixar `requirements-dev.txt` fora da análise. LOW/MEDIUM e achados
sem correção permanecem nos artifacts, mas não bloqueiam. Os relatórios são enviados
mesmo se o gate falhar. O Gitleaks oculta os valores dos segredos nos relatórios.

A imagem construída é testada em container e transferida como artifact para Syft,
Trivy e publicação. Apenas push aprovado na main publica no GHCR com tag sha-COMMIT.
Não há publicação em PR nem `continue-on-error` nos gates.

Artifacts: `gitleaks`, `cobertura`, `trivy-dependencias`, `trivy-imagem`, `sbom-spdx`.

## Configuração externa

- Projeto SonarCloud: `youserz_devopsPratica`, organização `youserz`.
- Secret GitHub `SONAR_TOKEN`; nunca armazenar seu valor em arquivos.
- Análise via CI e Quality Gate sobre código novo.
- Exigir os checks Gitleaks, Trivy dependencias, Testes e lint,
  SonarCloud Quality Gate, Construir e testar imagem e Trivy imagem e SBOM na main.
- PRs de forks não recebem secrets. Não usar pull_request_target para executar código de PRs.

## Demonstração

As evidências reais e links de execuções serão registrados em `docs/evidencias.md`.
O PR #2 da branch `demonstracao-cve` introduziu urllib3 1.26.4 no arquivo de
dependências de desenvolvimento para demonstrar o bloqueio. CVE-2021-33503 possui correção em 1.26.5.
Depois de registrar o relatório e o merge bloqueado, restaurar a versão fixada
atual no mesmo PR e guardar os checks aprovados. Não integrar a versão vulnerável.

## Executar os testes localmente

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/ruff check app tests
.venv/bin/pytest --cov=app --cov-report=xml
```

As capturas e os links reais estão em [evidencias.md](evidencias.md).
