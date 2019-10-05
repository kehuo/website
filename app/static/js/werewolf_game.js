/*
* @Author: Lucien Zhang
* @Date:   2019-09-29 18:02:32
* @Last Modified by:   Lucien Zhang
* @Last Modified time: 2019-10-04 20:11:56
*/


$.ajax({
        url: "werewolf/game_process",
        type: "GET",
        dataType: "json",
        success: function (data) {
            let info=$.parseJSON(data);

        }
        });

