<?php
if (isset($_POST['note'])) $_SESSION['notes'][] = $_POST['note'];
header("Location: /HakkaMD/?module=module/list.php");
