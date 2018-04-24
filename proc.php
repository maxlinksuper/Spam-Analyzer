<?php
    $command = $_POST["cmd"];
    $keywords = $_POST["key"];
    $posts = $_POST["posts"];

    $fp = fopen('post.json', 'w');
    fwrite($fp, json_encode($posts));
    fclose($fp);

    $file_command = fopen("command.txt", "w") or die("Unable to open file!");
    fwrite($file_command, $command);
    fclose($file_command);
    
    $file_keyword = fopen("keyword.txt", "w") or die("Unable to open file!");
    fwrite($file_keyword, $keywords);
    fclose($file_keyword);

    $result = exec('python algorithm.py '.$command.' '.$keywords );
    echo $result;
?>