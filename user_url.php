<?php
// user_url: http://<domínio>/deploy-atividade?invenira_instance_id=...
header('Content-Type: text/plain');
$invenira_instance_id = $_GET['invenira_instance_id'] ?? null;

if ($invenira_instance_id) {
    // Ação interna: Preparar-se para guardar analytics para esta instância da atividade.
    // Exemplo: Criar uma entrada na base de dados do AP para rastrear esta instância.
    // ...
    
    // Devolver o URL a ser usado pelos estudantes.
    $deployment_url = "http://<dominio_ap>/atividade_instancia/{$invenira_instance_id}";
    echo $deployment_url;
} else {
    http_response_code(400); // Bad Request
    echo "Erro: ID da instância da Inven!RA em falta.";
}
?>