<?php
// analytics_list_url: http://<domínio>/lista-analytics-atividade
header('Content-Type: application/json');
// Lista de todos os analytics que o AP recolhe, para o professor/formador associar a objetivos.
$analytics_list = [
    "qualAnalytics" => [
        ["name" => "Student activity profile", "type" => "URL"],
        ["name" => "Actitivy Heat Map", "type" => "URL"]
    ],
    "quantAnalytics" => [
        ["name" => "Acedeu à atividade", "type" => "boolean"],
        ["name" => "Download documento 1", "type" => "boolean"],
        ["name" => "Evolução pela atividade ()", "type" => "string"] // ou "float" dependendo do formato de 33.3
    ]
];
echo json_encode($analytics_list);
?>