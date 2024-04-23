$ (document).ready(function () {
    discordWidget.init({
        serverId: '831264892983050270',
        title: 'BerlinV',
        join: true,
        joinText: 'Server beitreten',
        alphabetical: false,
        theme: 'light',
        hideChannels: ['Channel Name 1', 'Channel Name 2'],
        showAllUsers: true,
        allUsersDefaultState: true,
        showNick: false,
        userName: '',
        useCDN: true
    });
    discordWidget.render();
});