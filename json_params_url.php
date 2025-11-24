<?php
// json_params_url: http://<dominio>/json-params-atividade
header('Content-Type: application/json');
$params = [
    ["name" => "resumo", "type" => "text/plain"], // Corresponde ao campo 'name="resumo"' no config_url.
    ["name" => "instrucoes", "type" => "text/plain"], // Corresponde ao campo 'name="instrucoes"'.
    ["name" => "versao_ap", "type" => "text/plain"] // Exemplo de campo hidden
];
echo json_encode($params);
?>