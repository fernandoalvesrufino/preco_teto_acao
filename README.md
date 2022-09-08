# Cálculo do preço teto de uma ação

Se você gosta de investimentos e acompanha um dos maiores investidores Pessoa Física da Bolsa brasileira, Luiz Barsi (AGF - Ações Garantem o Futuro), já deve ter ouvido falar do famoso **preço teto** de uma ação. Esse é o preço máximo que vale a pena comprar determinada ação visando um retorno de no mínimo 6% anual em dividendos.

Por isso, decidi fazer esse código acompanhando alguns canais do YouTube e TikTok que abordam o tema de finanças e programação em Python.

OBS: Esse é um código baseado no que o Barsi e a AGF _dizem_ que consideram como sendo o PREÇO TETO de uma ação. Os parâmetros utilizados foram obtidos através de vídeos e artigos apresentados pela AGF, mas não se trata do cálculo exato realizado por eles, afinal isso não é disponibilizado gratuitamente pela empresa. Para mais detalhes, ou para o cálculo exato, acesse diretamente a plataforma da AGF.

> Antes de replicar o código, não esqueça de importar a biblioteca _pandas_, instalar e importar a biblioteca _yfinance_:

```
import pandas as pd
!pip install yfinance
import yfinance as yf
```

## Explicação do programa:
No programa, basta digitar o código da empresa que deseja verificar (ex: BBAS3) e a porcentagem esperada dos dividendos (Ex: 6). Ao final, será apresentado o valor máximo para compra da ação. Caso a cotação atual exceda o indicado, a ação está cara demais! 

Bora pro código!
