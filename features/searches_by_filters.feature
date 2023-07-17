Feature: Buscas por filtrosss

    Os usuãrios poderão fazer buscas por reviews de músicas através de filtros de gênero, popularidade, nacionalidade e
    além de poderem escrever o nome de cantores, álbuns e músicas que querem encontrar suas respectivas reviews.

Scenario: Busca por gênero

Given o usuário “Ana” está na página de “Reviews”
And o usuário “Ana” quer achar a review de uma música do género POP
When o usuário “Ana” clica no “filtro” de busca
And o usuário “Ana” escolhe o gênero POP na categoria de “Gêneros” no filtro
Then a interface exibe os resultados filtrados de acordo com o gênero POP, mostrando as músicas e álbuns correspondentes.

Scenario : Busca por artista

Given o usuário “Ana” está na página de “Reviews”
And o usuário “Ana” quer achar a review de uma música da “Taylor Swift”
When o usuário “Ana” insere o nome da Taylor Swift em “buscar”
Then a interface apresenta os resultados filtrados, exibindo as músicas e álbuns da “Taylor Swift”