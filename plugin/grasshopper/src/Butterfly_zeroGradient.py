# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
zeroGradient boundary condition.

-
    Returns:
        zeroGradient: zeroGradient boundary condition.
"""

ghenv.Component.Name = "Butterfly_zeroGradient"
ghenv.Component.NickName = "zeroGradient"
ghenv.Component.Message = 'VER 0.0.04\nMAR_14_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "02::BoundaryCondition"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly.fields import ZeroGradient
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

zeroGradient = ZeroGradient()

