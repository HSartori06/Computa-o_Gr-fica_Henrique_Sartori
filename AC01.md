# AC01 — Estudo Dirigido 01
## Computação Visual: quatro áreas e aplicações

**Aluno(a):** [SEU NOME]  
**Turma:** [SUA TURMA]

## 1. Síntese de Imagens / Computação Gráfica

### Definição
Síntese de imagens é a área que produz imagens a partir de descrições matemáticas de cenas, objetos, câmeras, materiais e iluminação. Em vez de analisar uma imagem já existente, o sistema constrói uma nova imagem por meio de modelagem e renderização.

### Aplicação escolhida
**Renderização de um cubo 3D com PyOpenGL/Pygame.**

Repositório público utilizado como referência:
- `lau-est/PyOpengl` — projeto com exemplos de cubos 3D usando Python, Pygame e PyOpenGL.
- Link: https://github.com/lau-est/PyOpengl

### Principais aspectos
- representação geométrica por vértices, arestas e faces;
- projeção 3D para a tela 2D;
- transformações como rotação e translação;
- rasterização;
- aplicação de cores nas superfícies.

### Como executar
```bash
git clone https://github.com/lau-est/PyOpengl.git
cd PyOpengl
python -m pip install pygame PyOpenGL PyOpenGL_accelerate
python pygame1.py
```

### O que observar
Ao executar o exemplo, a imagem exibida não existia previamente: ela é sintetizada a partir da geometria do cubo, da câmera/projeção e das transformações aplicadas. Esse é o ponto central da Computação Gráfica.

**Evidência sugerida:** inserir uma captura da janela com o cubo renderizado.

---

## 2. Processamento de Imagens

### Definição
Processamento de imagens recebe uma imagem como entrada e produz outra imagem, normalmente com alguma alteração ou realce. São exemplos: filtragem, remoção de ruído, limiarização, erosão, dilatação, alteração de contraste e segmentação por intensidade/cor.

### Aplicação escolhida
**Limiarização/segmentação usando OpenCV.**

Repositório público utilizado:
- `opencv/opencv`
- Tutorial oficial de `inRange`, com exemplo em Python.
- Link do repositório: https://github.com/opencv/opencv

O exemplo oficial usa conversão para HSV e a função `cv.inRange()` para produzir uma máscara contendo apenas pixels dentro de uma faixa especificada.

### Principais aspectos
- a entrada é uma imagem ou quadro de vídeo;
- cada pixel é processado;
- o espaço de cores pode ser transformado, por exemplo, de BGR para HSV;
- o resultado também é uma imagem, normalmente uma máscara binária;
- não há necessariamente interpretação semântica do conteúdo.

### Como executar
```bash
git clone --depth 1 --branch 4.x https://github.com/opencv/opencv.git
python -m pip install opencv-python numpy
cd opencv/samples/python/tutorial_code/imgProc/threshold_inRange
python threshold_inRange.py
```

### O que observar
A imagem original é convertida para HSV e os pixels são classificados de acordo com limites de matiz, saturação e intensidade. O resultado é uma nova imagem/máscara. Isso caracteriza processamento de imagens.

**Evidência sugerida:** captura mostrando a imagem original e a máscara produzida.

---

## 3. Visão Computacional

### Definição
Visão computacional busca extrair informações e interpretar o conteúdo de imagens e vídeos. Diferentemente do processamento de imagens, o objetivo principal não é apenas produzir uma nova imagem, mas identificar objetos, padrões, posições ou eventos existentes nela.

### Aplicação escolhida
**Detecção de faces com OpenCV e classificador Haar Cascade.**

Repositório público:
- `StrixzIV/OpenCV-Face-Detection`
- Link: https://github.com/StrixzIV/OpenCV-Face-Detection

### Principais aspectos
- aquisição de imagem ou vídeo;
- extração e avaliação de características;
- uso de um classificador previamente treinado;
- detecção da posição de uma face;
- saída semântica: existe uma face e ela está em determinada região da imagem.

### Como executar
```bash
git clone https://github.com/StrixzIV/OpenCV-Face-Detection.git
cd OpenCV-Face-Detection
python -m pip install opencv-python
python detect.py
```

### O que observar
O programa analisa os pixels, mas o objetivo final é reconhecer uma entidade do mundo real — uma face — e marcar sua posição. Essa interpretação diferencia Visão Computacional de um simples filtro de imagem.

**Evidência sugerida:** captura com um retângulo indicando uma face detectada.

---

## 4. Visualização Computacional

### Definição
Visualização computacional transforma dados abstratos ou científicos em representações gráficas que facilitem a interpretação humana. A entrada pode ser uma tabela, uma função matemática, medições ou resultados de uma simulação.

### Aplicação escolhida
**Visualização de dados com Matplotlib.**

Repositório público:
- `matplotlib/matplotlib`
- Link: https://github.com/matplotlib/matplotlib

O projeto possui uma galeria extensa de exemplos de gráficos 2D e 3D.

### Principais aspectos
- mapeamento de dados para posições, tamanhos e símbolos gráficos;
- criação de eixos, escalas e legendas;
- comparação de valores;
- identificação visual de padrões, tendências e relações;
- possibilidade de visualização 2D ou 3D.

### Exemplo simples para execução
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 4, 8, 10]

plt.plot(x, y, marker="o")
plt.xlabel("Amostra")
plt.ylabel("Valor")
plt.title("Visualização de dados")
plt.grid(True)
plt.show()
```

Instalação:
```bash
python -m pip install matplotlib
```

### O que observar
Os números do conjunto de dados são convertidos em posições gráficas. O gráfico facilita perceber crescimento e variações que seriam menos evidentes observando apenas a lista numérica.

**Evidência sugerida:** captura do gráfico resultante.

---

## 5. Comparação das quatro áreas

| Área | Entrada típica | Objetivo principal | Saída típica |
|---|---|---|---|
| Síntese de Imagens | modelos, geometria, câmera | criar uma imagem | imagem renderizada |
| Processamento de Imagens | imagem | alterar/melhorar a imagem | nova imagem |
| Visão Computacional | imagem/vídeo | interpretar o conteúdo | informação sobre objetos/padrões |
| Visualização Computacional | dados | facilitar interpretação humana | gráfico/representação visual |

## Conclusão

As quatro áreas trabalham com informação visual, porém têm objetivos diferentes. Na síntese de imagens, uma imagem é criada a partir de uma cena ou modelo. No processamento de imagens, uma imagem existente é modificada. Na visão computacional, imagens são analisadas para obter informações sobre seu conteúdo. Na visualização computacional, dados são convertidos em uma representação gráfica para facilitar a análise humana.

## Referências
- PyOpenGL/Pygame example: https://github.com/lau-est/PyOpengl
- OpenCV: https://github.com/opencv/opencv
- OpenCV Face Detection example: https://github.com/StrixzIV/OpenCV-Face-Detection
- Matplotlib: https://github.com/matplotlib/matplotlib
