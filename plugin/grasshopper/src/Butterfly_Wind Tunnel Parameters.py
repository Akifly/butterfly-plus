# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Wind tunnel parameters.

-

    Args:
        _windwardX_: Multiplier value for windward extension (default: 3).
        _topX_: Multiplier value for top extension (default: 5).
        _sideX_: Multiplier value for side extension (default: 5).
        _leewardX_: Multiplier value for leeward extension (default: 15).
    Returns:
        readMe!: Reports, errors, warnings, etc.
        tunnelParams: Tunnel Parameters
"""

ghenv.Component.Name = "Butterfly_Wind Tunnel Parameters"
ghenv.Component.NickName = "tunnelParams"
ghenv.Component.Message = 'VER 0.0.04\nOCT_07_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from butterfly.windtunnel import TunnelParameters
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

tunnelParams = TunnelParameters(_windwardX_, _topX_, _sidesX_, _leewardX_)
