<?php
// config_url: http://<dominio>/configuracao-atividade.html
header('Content-Type: text/html');
echo '
<form id="configForm">
    <label for="resumo">Resumo da Descrição Técnica:</label>
    <textarea name="resumo" id="resumo" rows="4" cols="50"></textarea><br><br>
    <label for="instrucoes">URL para Instruções Detalhadas:</label>
    <input type="url" name="instrucoes" id="instrucoes"><br><br>
    <input type="hidden" name="versao_ap" value="1.0">
</form>
';
// Não tem botão "OK" ou "Guardar", a Inven!RA é que recolhe os valores.
?>