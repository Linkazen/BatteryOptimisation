<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EPEnergy</title>
    <link rel="stylesheet" type="text/css" href="./style.css">
</head>
<body>

    <h1 id="title">EASTER PARKGATE ENERGY</h1>

    <div id="container">
        <div class="scroll" id="priceContainer">
            <div class="price">
                <div class="priceItems">Time:</div>
                <div class="priceItems">Price:<br>(p kw/h)</div>
            </div>

            <?php
                $tariff = json_decode(file_get_contents("../InverterInfo/Tariffs.json"), true)["results"];
                for ($x = 0; $x < sizeof($tariff); $x++) {
            ?>
                <div class="price">
                    <div class="priceItems"><?php echo substr($tariff[$x]["valid_from"], 11, 5)?></div>
                    <div class="priceItems"><?php echo number_format($tariff[$x]["value_inc_vat"], 2)?></div>
                </div>
            <?php
                }
            ?>
        </div>
    </div>

    <script src="./script.js"></script>
</body>
</html>