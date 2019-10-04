/*
 * @Author: Lucien Zhang
 * @Date:   2019-10-04 16:47:05
 * @Last Modified by:   Lucien Zhang
 * @Last Modified time: 2019-10-04 17:43:09
 */
document.querySelector("#game_form").onsubmit = function() {
    let msg = ""
    let victory_mode = $('#victoryModeGroup input[name="victoryMode"]:checked').val();

    if (victory_mode === 'kill_group') {
        victory_mode = '屠边';
    } else if (victory_mode === 'kill_all') {
        victory_mode = '屠城';
    }
    msg += '游戏模式为：' + victory_mode + '\n';

    let villager = $('#villager option:selected').val();
    let normal_wolf = $('#normal_wolf option:selected').val();

    let role_cnt = parseInt(villager) + parseInt(normal_wolf);
    let single_roles = "";

    $('input[name="single_roles"]:checked').each(function() {
        // console.log($(this).next());
        single_roles += $(this).next().text() + ' = 1\n';
        role_cnt += 1;
    });
    msg += '游戏总人数为：' + role_cnt.toString() + '人\n';
    msg += '普通村民 = ' + villager + '\n';
    msg += '普通狼人 = ' + normal_wolf + '\n';
    msg += single_roles;

    return confirm(msg)

    // if (document.querySelector('#confirm').value != document.querySelector('#password').value) {
    //     alert("两次输入的密码不一致!");
    //     return false;
    // }
};
