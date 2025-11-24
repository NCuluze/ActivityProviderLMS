<?php
// analytics_url: http://<dominio>/analytics-atividade
header('Content-Type: application/json');
$input_json = file_get_contents('php://input');
$data = json_decode($input_json, true);
$activity_id = $data['activityID'] ?? null; // ID da Inven!RA.

if ($activity_id) {
    // Ação interna: Obter analytics de TODOS os alunos para esta activityID.
    // (Simulação de dados de resposta - o formato final deve corresponder ao esperado)
    $analytics_response = [
        [
            "inveniraStdID" => "1001",
            "quantAnalytics" => [
                ["name" => "Acedeu à atividade", "value" => true],
                ["name" => "Download documento 1", "value" => true],
                ["name" => "Evolução pela atividade ()", "value" => "33.3"]
            ],
            "qualAnalytics" => [
                "Student activity profile" => "https://ActivityProvider/?APAnID=11111111", // URL para o AP devolver a página de conteúdo qualitativo.
                "Actitivy Heat Map" => "https://ActivityProvider/?APAnID=21111111"
            ]
        ],
        // ... outros utilizadores
    ];
    
    echo json_encode($analytics_response);
} else {
    http_response_code(400);
    echo json_encode(["error" => "activityID em falta."]);
}
?>