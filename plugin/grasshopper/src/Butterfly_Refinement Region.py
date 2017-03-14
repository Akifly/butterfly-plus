# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Butterfly refinement range.

-

    Args:
        _geo: Grasshopper geometries.
        _name: Surface name.
        _refMode: Refinement mode. Used locationRefMode or distanceRefMode components.
        _meshSet_: Grasshopper mesh settings.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        refinementRegion: A Buttefly refinement region.
"""

ghenv.Component.Name = "Butterfly_Refinement Region"
ghenv.Component.NickName = "refinementRegion"
ghenv.Component.Message = 'VER 0.0.04\nMAR_14_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "4"

try:
    from butterfly_grasshopper.refinementRegion import RefinementRegionGH
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _geo and _name and _refMode:
    refinementRegion = RefinementRegionGH(_name, _geo, _refMode, _meshSet_)
