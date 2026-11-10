# frentia-midia
Imagens dos posts do Frentia (gestão de serviços: equipes, mão de obra e atividades) nas redes sociais, geradas pelo agente de conteúdo.

## Regras obrigatórias (Manual da Marca, `modelos/manual-da-marca.pdf`)
- **Sempre** usar o logotipo oficial: `modelos/assets/frentia-logo.png` em fundos claros; `modelos/assets/frentia-logo-negativo.png` em fundo Azul Frentia. Nunca recriar o wordmark com fonte, distorcer, aplicar sombra/contorno ou colocar sobre fundo de baixo contraste. Altura de 84px no post (≈325px de largura) e área de respiro livre ao redor.
- Cores: Azul Frentia #002F6C (dominante), Azul Operacional #0B4A8F (apoio), Laranja Avanço #FF6B00 (só CTA/destaques pontuais), Cinza Grafite #263238 (texto), Cinza Campo #EEF2F6 (fundos/cards), borda #D7DEE8. Cores de status (verde #2E7D32, amarelo #F9A825, vermelho #C62828) só com significado operacional.
- Tipografia: títulos em Manrope (assets/), texto em Inter. Cards com raio 14px, botões com raio 10px.
- Tom: objetivo, operacional, seguro; verbos de ação.

## Como gerar
- Modelos em `modelos/` (`card-impacto.html`, `passo-a-passo.html`, `destaque-azul.html`) usando `modelos/base.css`. Copie um modelo para `modelos/_tmp.html` (precisa ficar em `modelos/` por causa dos caminhos relativos), edite os textos e rode `python3 modelos/render.py modelos/_tmp.html posts/AAAA-MM-DD-slug.jpg`. Apague o `_tmp.html` depois.
- Link público: https://raw.githubusercontent.com/luismattos-sketch/frentia-midia/main/posts/<arquivo>
