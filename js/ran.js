$ (document).ready(function () {
    "use strict";
    var polShow = false;
    var maltShow = false;
    var feuerShow = false;
    var adacShow = false;
    var mafiaShow = false;
    var formShow = {
        "polizei": false,
        "malteser": true,
        "feuerwehr": true,
        "adac": true,
        "mafia": false,
        "zoll": false,
    };

    if (formShow.polizei == false) {
        $ ("#polizei").hide();
    };
    if (formShow.malteser == false) {
        $ ("#malteser").hide();
    };
    if (formShow.feuerwehr == false) {
        $ ("#feuerwehr").hide();
    };    
    if (formShow.adac == false) {
        $ ("#adac").hide();
    };
    if (formShow.mafia == false) {
        $ ("#mafia").hide();
    };
    if (formShow.zoll == false) {
        $ ("#zoll").hide();
    };

    $ ("#polForm").hide();
    $ ("#malteserForm").hide();
    $ ("#feuerwehrForm").hide();
    $ ("#adacForm").hide();
    $ ("#mafiaForm").hide();
    $ ("#zollForm").hide();

    $ ("#polizei").click(function() {
        if (polShow == false) {
            $ ("#polForm").slideDown("slow");
            polShow = true;
        } else {
            $ ("#polForm").slideUp("slow");
            polShow = false;
        };
    });

    $ ("#malteser").click(function() {
        if (maltShow == false) {
            $ ("#malteserForm").slideDown("slow");
            maltShow = true;
        } else {
            $ ("#malteserForm").slideUp("slow");
            maltShow = false;
        };
    })

    $ (".malteserP2").hide();
    $ (".malteserP3").hide();
    $ (".malteserP4").hide();
    $ (".malteserP5").hide();

    $ ("#malteserP1Weiter").click(function() {
        $ (".malteserP1").slideUp("slow");
        $ (".malteserP2").slideDown("slow");
    });
    $ ("#malteserP2Weiter").click(function() {
        $ (".malteserP2").slideUp("slow");
        $ (".malteserP3").slideDown("slow");
    });
    $ ("#malteserP3Weiter").click(function() {
        $ (".malteserP3").slideUp("slow");
        $ (".malteserP4").slideDown("slow");
    });    
    $ ("#malteserP4Weiter").click(function() {
        $ (".malteserP4").slideUp("slow");
        $ (".malteserP5").slideDown("slow");
    });

    $ ("#feuerwehr").click(function() {
        if (feuerShow == false) {
            $ ("#feuerwehrForm").slideDown("slow");
            feuerShow = true;
        } else {
            $ ("#feuerwehrForm").slideUp("slow");
            feuerShow = false;
        };
    });

    $ (".feuerP2").hide();
    $ (".feuerP3").hide();
    $ (".feuerP4").hide();

    $ ("#feuerP1Weiter").click(function() {
        $ (".feuerP1").slideUp("slow");
        $ (".feuerP2").slideDown("slow");
    });
    $ ("#feuerP2Weiter").click(function() {
        $ (".feuerP2").slideUp("slow");
        $ (".feuerP3").slideDown("slow");
    });
    $ ("#feuerP3Weiter").click(function() {
        $ (".feuerP3").slideUp("slow");
        $ (".feuerP4").slideDown("slow");
    });
    
    $ ("#adac").click(function() {
        if (adacShow == false) {
            $ ("#adacForm").slideDown("slow");
            adacShow = true;
        } else {
            $ ("#adacForm").slideUp("slow");
            adacShow = false;
        };
    });

    $ (".adacP2").hide();

    $ ("#adacP1Weiter").click(function() {
        $ (".adacP1").slideUp("slow");
        $ (".adacP2").slideDown("slow");
    });
});