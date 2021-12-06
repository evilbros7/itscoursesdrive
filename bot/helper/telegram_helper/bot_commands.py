import os

from bot import BOT_NO

def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command
class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand('START_COMMAND', f'start{BOT_NO}')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', f'mirror{BOT_NO}')
        self.UnzipMirrorCommand = getCommand('UNZIPMIRROR_COMMAND', f'unzipmirror{BOT_NO}')
        self.ZipMirrorCommand = getCommand('ZIPMIRROR_COMMAND', f'zipmirror{BOT_NO}')
        self.CancelMirror = getCommand('CANCELMIRROR_COMMAND', f'cancel{BOT_NO}')
        self.CancelAllCommand = getCommand('CANCELALL_COMMAND', f'cancelall{BOT_NO}')
        self.ListCommand = getCommand('LIST_COMMAND', f'list{BOT_NO}')
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'search{BOT_NO}')
        self.StatusCommand = getCommand('STATUS_COMMAND', f'status{BOT_NO}')
        self.AuthorizedUsersCommand = getCommand('AUTHORIZEDUSERS_COMMAND', f'users{BOT_NO}')
        self.AuthorizeCommand = getCommand('AUTHORIZE_COMMAND', f'authorize{BOT_NO}')
        self.UnAuthorizeCommand = getCommand('UNAUTHORIZE_COMMAND', f'unauthorize{BOT_NO}')
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', f'addsudo{BOT_NO}')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', f'rmsudo{BOT_NO}')
        self.PingCommand = getCommand('PING_COMMAND', f'ping{BOT_NO}')
        self.RestartCommand = getCommand('RESTART_COMMAND', f'restart{BOT_NO}')
        self.RebootCommand = getCommand('REBOOT_COMMAND', f'reboot{BOT_NO}')
        self.StatsCommand = getCommand('STATS_COMMAND', f'stats{BOT_NO}')
        self.HelpCommand = getCommand('HELP_COMMAND', f'help{BOT_NO}')
        self.LogCommand = getCommand('LOG_COMMAND', f'log{BOT_NO}')
        self.SpeedCommand = getCommand('SPEED_COMMAND', f'speedtest{BOT_NO}')
        self.CloneCommand = getCommand('CLONE_COMMAND', f'clone{BOT_NO}')
        self.CountCommand = getCommand('COUNT_COMMAND', f'count{BOT_NO}')
        self.WatchCommand = getCommand('WATCH_COMMAND', f'watch{BOT_NO}')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', f'zipwatch{BOT_NO}')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', f'qbmirror{BOT_NO}')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIPMIRROR_COMMAND', f'qbunzipmirror{BOT_NO}')
        self.QbZipMirrorCommand = getCommand('QBZIPMIRROR_COMMAND', f'qbzipmirror{BOT_NO}')
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'del{BOT_NO}')
        self.ConfigMenuCommand = getCommand('CONFIGMENU_COMMAND', f'config{BOT_NO}')
        self.UsageCommand = getCommand('USAGE_COMMAND', f'usage{BOT_NO}')
        self.ShellCommand = getCommand('SHELL_COMMAND', f'shell{BOT_NO}')
        self.TsHelpCommand = getCommand('TSHELP_COMMAND', f'tshelp{BOT_NO}')
        self.ExecHelpCommand = getCommand('EXECHELP_COMMAND', f'exechelp{BOT_NO}')
        self.RssHelpCommand = getCommand('RSSHELP_COMMAND', f'rsshelp{BOT_NO}')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', f'leechset{BOT_NO}')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', f'setthumb{BOT_NO}')
        self.LeechCommand = getCommand('LEECH_COMMAND', f'leech{BOT_NO}')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', f'unzipleech{BOT_NO}')
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', f'zipleech{BOT_NO}')
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', f'qbleech{BOT_NO}')
        self.QbUnzipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', f'qbunzipleech{BOT_NO}')
        self.QbZipLeechCommand = getCommand('QBZIPLEECH_COMMAND', f'qbzipleech{BOT_NO}')
        self.LeechWatchCommand = getCommand('LEECHWATCH_COMMAND', f'leechwatch{BOT_NO}')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', f'leechzipwatch{BOT_NO}')

BotCommands = _BotCommands()
