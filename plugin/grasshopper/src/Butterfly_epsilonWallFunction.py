# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
epsilonWallFunction boundary condition.

-
    Args:
        _value: input value.
        _Cmu_:
        _kappa_:
        _E_:
    Returns:
        epsilonWallFunction: epsilonWallFunction boundary condition.
"""

ghenv.Component.Name = "Butterfly_epsilonWallFunction"
ghenv.Component.NickName = "epsilonWallFunction"
ghenv.Component.Message = 'VER 0.0.04\nMAR_14_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "02::BoundaryCondition"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly.fields import EpsilonWallFunction
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _value:
    epsilonWallFunction = EpsilonWallFunction(_value, _Cmu_, _kappa_, _E_)

