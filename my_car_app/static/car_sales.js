document.addEventListener('DOMContentLoaded', function() {
    // Obter todos os botões de comprar
    const botoes = document.querySelectorAll('.btn-comprar');
    
    botoes.forEach(botao => {
        botao.addEventListener('click', function(e) {
            // Evitar ação padrão se o botão estiver desabilitado
            if (this.disabled) {
                e.preventDefault();
                return;
            }
            
            // Obter a linha da tabela (tr) do botão clicado
            const linha = this.closest('tr');
            
            if (linha) {
                // Extrair dados da linha
                const colunas = linha.querySelectorAll('td');
                const marca = colunas[1].textContent.trim();
                const modelo = colunas[2].textContent.trim();
                
                // Mostrar alerta com as informações
                alert(`✓ Carro vendido!\n\nMarca: ${marca}\nModelo: ${modelo}`);
                
                // Opcional: mudar o status do carro para "Vendido"
                const statusCell = colunas[6];
                const botaoAcao = colunas[7];
                
                // Atualizar o status
                statusCell.innerHTML = '<span class="status vendido">Vendido</span>';
                
                // Desabilitar o botão
                this.disabled = true;
                this.textContent = 'Vendido';
                this.style.opacity = '0.5';
                this.style.cursor = 'not-allowed';
            }
        });
    });
});
