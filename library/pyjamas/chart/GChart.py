"""
* Copyright 2007,2008,2009 John C. Gunther
* Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
*
* Licensed under the Apache License, Version 2.0 (the
* "License"); you may not use this file except in compliance
* with the License. You may obtain a copy of the License at:
*
*  http:#www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing,
* software distributed under the License is distributed on an
* "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
* either express or implied. See the License for the specific
* language governing permissions and limitations under the
* License.
*
"""




from pyjamas import DOM
from pyjamas import Window



























from pyjamas.ui import Event
from pyjamas.ui.AbsolutePanel import AbsolutePanel
from pyjamas.ui.Composite import Composite
from pyjamas.ui.Grid import Grid
from pyjamas.ui import HasHorizontalAlignment
from pyjamas.ui import HasVerticalAlignment
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Image import Image
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.UIObject import UIObject
from pyjamas.ui.Widget import Widget

"""*
* Convenience method that, given a plain text label, returns an
* HTML snippet appropriate for use as an argument to the
* <tt>setHovertextTemplate</tt> or <tt>setAnnotationText</tt>
* methods, that will display the plain text label with
* formatting appropriate for use with hovertext.
*
* @see Symbol#setHovertextTemplate setHovertextTemplate
* @see Curve.Point#setAnnotationText setAnnotationText
* @see Symbol#setHoverAnnotationSymbolType setHoverAnnotationSymbolType
*
* @param plainTextLabel the plain text label that is to be
*  HTML-wrapped to make it look like <tt>setTitle</tt>-based
*  hovertext.
*
*
"""

def formatAsHovertext(self, plainTextLabel):
    result = \
    "<html><div style='background-color:#FFFFF0; border-color:black; border-style:solid; border-width:1px 1px 1px 1px; padding:2px; text-align:left'>"
    + plainTextLabel + "</div>"
    return result


"""* Default size, in pixels, of text used to annotate individual
** plotted points on a curve.
**
** @see Curve.Point#setFontSize Point.setFontSize
"""
DEFAULT_ANNOTATION_FONTSIZE = 12

"""*
* Default pixel height of rectangular "brush" that defines
* how close the mouse cursor must be to a rendered symbol for
* it to be "touched" (which pops up its hover feedback).
*
* @see Symbol#setBrushHeight setBrushHeight
* @see Symbol#setBrushWidth setBrushWidth
* @see #DEFAULT_BRUSH_WIDTH DEFAULT_BRUSH_WIDTH
"""
DEFAULT_BRUSH_HEIGHT = 1
"""*
*
* Default pixel width of rectangular "brush" that defines how
* close the mouse cursor must be to a rendered symbol for it
* to be "touched" (which pops up its hover feedback).
*
* @see Symbol#setBrushHeight setBrushHeight
* @see Symbol#setBrushWidth setBrushWidth
* @see #DEFAULT_BRUSH_HEIGHT DEFAULT_BRUSH_HEIGHT
"""
DEFAULT_BRUSH_WIDTH = 1

"""* Default color of border around the chart legend
**
** @see #setLegendBorderColor setLegendBorderColor
**
*"""
DEFAULT_LEGEND_BORDER_COLOR = "black"
"""* Default width of border around the chart legend
**
** @see #setLegendBorderWidth setLegendBorderWidth
**
*"""
DEFAULT_LEGEND_BORDER_WIDTH = 1
"""* Default style of border around the chart legend
**
** @see #setLegendBorderStyle setLegendBorderStyle
**
*"""
DEFAULT_LEGEND_BORDER_STYLE = "solid"

"""* Default color of background of the chart legend
**
** @see #setLegendBackgroundColor setLegendBackgroundColor
**
"""
DEFAULT_LEGEND_BACKGROUND_COLOR = "transparent"
"""*
** The default color of any text appearing in a chart's
** legend, annotations, or tick labels.
**
** @see #setLegendFontColor setLegendFontColor
** @see Axis#setTickLabelFontColor setTickLabelFontColor
** @see Curve.Point#setAnnotationFontColor setAnnotationFontColor
**
*"""
DEFAULT_FONT_COLOR ="black"
"""*
** Default style of axis label and legend fonts.
**
** @see #setLegendFontStyle setLegendFontStyle
** @see Axis#setTickLabelFontStyle setTickLabelFontStyle
** @see Curve.Point#setAnnotationFontStyle
** setAnnotationFontStyle
**
*"""
DEFAULT_FONT_STYLE = "normal"
"""* Default weight of axis label and legend fonts.
**
** @see #setLegendFontWeight setLegendFontWeight
** @see Axis#setTickLabelFontWeight setTickLabelFontWeight
** @see Curve.Point#setAnnotationFontWeight
** setAnnotationFontWeight
**
*"""

DEFAULT_FONT_WEIGHT = "normal"

"""*
** The default template string used to generate the hovertext
** displayed when the user hovers their mouse above a point
** on a curve (pie slices have a different default).
**
** @see Symbol#setHovertextTemplate setHovertextTemplate
** @see #DEFAULT_PIE_SLICE_HOVERTEXT_TEMPLATE
**    DEFAULT_PIE_SLICE_HOVERTEXT_TEMPLATE
**
"""
DEFAULT_HOVERTEXT_TEMPLATE = formatAsHovertext("(${x}, ${y})")
"""*
** The default hover feedback location used to position the
** hover feedback when the user hovers their mouse above a point
** on a curve (pie slices, and bar symbols have different
** defaults).
**
** @see Symbol#setHoverLocation setHoverLocation
** @see #DEFAULT_PIE_SLICE_HOVER_LOCATION DEFAULT_PIE_SLICE_HOVER_LOCATION
** @see #DEFAULT_VBAR_BASELINE_HOVER_LOCATION DEFAULT_VBAR_BASELINE_HOVER_LOCATION
** @see #DEFAULT_VBARBOTTOM_HOVER_LOCATION DEFAULT_VBARBOTTOM_HOVER_LOCATION
** @see #DEFAULT_VBARTOP_HOVER_LOCATION DEFAULT_VBARTOP_HOVER_LOCATION
** @see #DEFAULT_HBAR_BASELINE_HOVER_LOCATION DEFAULT_HBAR_BASELINE_HOVER_LOCATION
** @see #DEFAULT_HBARLEFT_HOVER_LOCATION DEFAULT_HBARLEFT_HOVER_LOCATION
** @see #DEFAULT_HBARRIGHT_HOVER_LOCATION DEFAULT_HBARRIGHT_HOVER_LOCATION
**
"""
DEFAULT_HOVER_LOCATION = AnnotationLocation.NORTHWEST
"""* The default fontsize of text that appears
** in the chart's legend (key).
**
** @see Axis#setTickLabelFontSize setTickLabelFontSize
** @see #getXAxis getXAxis
** @see #getYAxis getYAxis
** @see #getY2Axis getY2Axis
**
*"""
DEFAULT_LEGEND_FONTSIZE = 12


"""*
** The default background color used for the chart's plot area
** if none is specified.
**
** @see #setPlotAreaBackgroundColor setPlotAreaBackgroundColor
**
*"""
DEFAULT_PLOTAREA_BACKGROUND_COLOR = "transparent"
"""*
** The default border color used for the chart's plot area
** if none is specified.
**
** @see #setPlotAreaBorderColor setPlotAreaBorderColor
**
*"""
DEFAULT_PLOTAREA_BORDER_COLOR = "black"
"""*
** The default style of the border around the chart's plot area
** if none is specified.
**
** @see #setPlotAreaBorderStyle setPlotAreaBorderStyle
**
*"""
DEFAULT_PLOTAREA_BORDER_STYLE = "solid"
"""*
** The default width of the border around the chart's plot area
** if none is specified.
**
** @see #setPlotAreaBorderWidth setPlotAreaBorderWidth
**
*"""
DEFAULT_PLOTAREA_BORDER_WIDTH = 0
"""*
** The default CSS background color used for symbols if none is
** specified.
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setBackgroundColor setBackgroundColor
*"""
DEFAULT_SYMBOL_BACKGROUND_COLOR = "transparent"
"""*
** The default CSS border colors used for symbols if none are
** specified. These defaults are, in order of the curve's
** integer index: red, green, blue, fuchsia, aqua, teal,
** maroon, lime, navy, silver, olive, purple.  This sequence
** repeats if there are more than 12 curves.
** <p>
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setBorderColor setBorderColor
**
*"""

DEFAULT_SYMBOL_BORDER_COLORS = \
                ["red", "green", "blue",
                "fuchsia", "aqua", "teal",
                "maroon", "lime", "navy",
                "silver", "olive", "purple"]

"""*
** The default CSS border style used for symbols if none is
** specified; this default is "solid".
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setBorderStyle setBorderStyle
**
*"""
DEFAULT_SYMBOL_BORDER_STYLE = "solid"
"""*
** The default CSS border width used for symbols if none is
** specified; this default is 1 pixel.
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setBorderWidth setBorderWidth
**
*"""
DEFAULT_SYMBOL_BORDER_WIDTH = 1
"""*
** The default spacing between discrete, rectangular, elements
** used to simulate continuous graphical elements. This
** default does not apply to bar chart symbol types or
** the LINE symbol type, which have their own default
** fill spacings.
** <p>
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setFillSpacing setFillSpacing
** @see Symbol#setFillThickness setFillThickness
** @see #DEFAULT_BAR_FILL_SPACING
**      DEFAULT_BAR_FILL_SPACING
** @see #DEFAULT_LINE_FILL_SPACING
**      DEFAULT_LINE_FILL_SPACING
**
*"""
DEFAULT_SYMBOL_FILL_SPACING = 4
"""*
** The default "thickness" of the rectangular elements used to
** simulate continuous graphical objects, such as connecting
** lines in line charts. This default applies to all symbol
** types <tt>except</tt> for those representing pie slices,
** whose default is
** <tt>DEFAULT_PIE_SLICE_FILL_THICKNESS</tt>, and the LINE
** symbol type, whose default is DEFAULT_LINE_FILL_THICKNESS.
**
** <p> Since this default thickness is 0 px, this implies
** that, except for pie slices and lines, no such continuous fill
** elements are generated by default. For example, if you
** want to have dotted connecting lines drawn between individual
** data points represented using the <tt>BOX_CENTER</tt>
** symbol type, you must explicitly specify a positive fill
** thickness (for solid connecting lines, the LINE symbol
** is usually far more efficient than using a fill thickness
** of 1px with the BOX_CENTER symbol).
**
** @see #DEFAULT_PIE_SLICE_FILL_THICKNESS
**      DEFAULT_PIE_SLICE_FILL_THICKNESS
** @see #DEFAULT_LINE_FILL_THICKNESS
**      DEFAULT_LINE_FILL_THICKNESS
** @see Curve#getSymbol getSymbol
** @see Symbol#setFillSpacing setFillSpacing
** @see Symbol#setFillThickness setFillThickness
**
*"""
DEFAULT_SYMBOL_FILL_THICKNESS = 0


"""*
** The default spacing between discrete, rectangular, elements
** used to simulate continuous filling of polygonal regions
** formed by connecting corresponding ends of successive
** bars in a bar chart.
** <p>
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setFillSpacing setFillSpacing
** @see Symbol#setFillThickness setFillThickness
** @see #DEFAULT_SYMBOL_FILL_SPACING DEFAULT_SYMBOL_FILL_SPACING
**
*"""
DEFAULT_BAR_FILL_SPACING = 0

"""*
** The default thickness of connecting lines drawn on
** curves whose symbols have the LINE symbol type.
**
** @see #DEFAULT_SYMBOL_FILL_THICKNESS
**      DEFAULT_SYMBOL_FILL_THICKNESS
** @see Curve#getSymbol getSymbol
** @see Symbol#setFillSpacing setFillSpacing
** @see Symbol#setFillThickness setFillThickness
**
*"""
DEFAULT_LINE_FILL_THICKNESS = 1


"""*
** The default spacing between discrete, rectangular, elements
** used to simulate continuously connected lines between
** successive points on a curve that uses the
** <tt>LINE</tt> symbol type.
** <p>
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setFillSpacing setFillSpacing
** @see Symbol#setFillThickness setFillThickness
** @see #DEFAULT_SYMBOL_FILL_SPACING DEFAULT_SYMBOL_FILL_SPACING
**
*"""
DEFAULT_LINE_FILL_SPACING = 0

"""*
** The default "spacing" between corresponding edges of the
** rectangular elements used to simulate continuous fill of pie
** slices.  <p>
**
** @see #DEFAULT_SYMBOL_FILL_SPACING
**      DEFAULT_SYMBOL_FILL_SPACING
** @see #DEFAULT_PIE_SLICE_FILL_THICKNESS
**      DEFAULT_PIE_SLICE_FILL_THICKNESS
** @see Curve#getSymbol getSymbol
** @see Symbol#setFillSpacing setFillSpacing
** @see Symbol#setFillThickness setFillThickness
**
*"""
DEFAULT_PIE_SLICE_FILL_SPACING = 4
"""*
** The default "thickness" of the rectangular elements
** used to simulate continuous fill of pie slices. This
** thickness defines the height of horizontal pie slice
** shading bars, and the width of vertical shading bars.
** <p>
**
** @see #DEFAULT_SYMBOL_FILL_THICKNESS
**      DEFAULT_SYMBOL_FILL_THICKNESS
** @see #DEFAULT_LINE_FILL_THICKNESS
**      DEFAULT_LINE_FILL_THICKNESS
** @see Curve#getSymbol getSymbol
** @see Symbol#setFillSpacing setFillSpacing
** @see Symbol#setFillThickness setFillThickness
**
*"""
DEFAULT_PIE_SLICE_FILL_THICKNESS = 2

"""*
** The default hovertext template used by symbols when they have a
** symbol type of of the form PIE_SLICE_*.
**
** @see Symbol#setHovertextTemplate setHovertextTemplate
** @see SymbolType#PIE_SLICE_OPTIMAL_SHADING PIE_SLICE_OPTIMAL_SHADING
** @see #DEFAULT_HOVERTEXT_TEMPLATE DEFAULT_HOVERTEXT_TEMPLATE
**
*"""
DEFAULT_PIE_SLICE_HOVERTEXT_TEMPLATE = formatAsHovertext("${pieSliceSize}")

"""*
** The default hover feedback location used by symbols when they have a
** symbol type of of the form PIE_SLICE_*.
**
** @see Symbol#setHoverLocation setHoverLocation
** @see #DEFAULT_HOVER_LOCATION DEFAULT_HOVER_LOCATION
**
*"""
DEFAULT_PIE_SLICE_HOVER_LOCATION = AnnotationLocation.OUTSIDE_PIE_ARC
"""*
** The default height (including borders) used for
** symbols if none is specified; this default is
** the same as for <tt>DEFAULT_SYMBOL_WIDTH</tt>
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setHeight setHeight
** @see #DEFAULT_SYMBOL_WIDTH DEFAULT_SYMBOL_WIDTH
**
*"""
DEFAULT_SYMBOL_HEIGHT = 7

"""*
** The default symbol type for curve if none is
** specified; this default is BOX_CENTER
**
** @see SymbolType#BOX_CENTER BOX_CENTER
** @see Symbol#setSymbolType setSymbolType
**
*"""
DEFAULT_SYMBOL_TYPE = SymbolType.BOX_CENTER

"""*
** The default width (including borders) used for
** symbols if none is specified.
**
** @see Curve#getSymbol getSymbol
** @see Symbol#setWidth setWidth
** @see #DEFAULT_SYMBOL_WIDTH DEFAULT_SYMBOL_WIDTH
*"""
DEFAULT_SYMBOL_WIDTH = DEFAULT_SYMBOL_HEIGHT

"""*
* The default number of tick marks on each Axis.
*
* @see Axis#setTickCount setTickCount
*
"""
DEFAULT_TICK_COUNT = 10

"""* The default color (a CSS color specification) of tick labels
**
** @see Axis#setTickLabelFontColor setTickLabelFontColor
** @see #getXAxis getXAxis
** @see #getYAxis getYAxis
** @see #getY2Axis getY2Axis
*"""
DEFAULT_TICK_LABEL_FONT_COLOR ="black"

"""* The default CSS font-style applied to tick labels
**
** @see Axis#setTickLabelFontStyle setTickLabelFontStyle
** @see #getXAxis getXAxis
** @see #getYAxis getYAxis
** @see #getY2Axis getY2Axis
*"""
DEFAULT_TICK_LABEL_FONT_STYLE ="normal"

"""* The default CSS font-weight applied to tick labels
**
** @see Axis#setTickLabelFontWeight setTickLabelFontWeight
** @see #getXAxis getXAxis
** @see #getYAxis getYAxis
** @see #getY2Axis getY2Axis
*"""
DEFAULT_TICK_LABEL_FONT_WEIGHT ="normal"


"""* The default fontsize (in pixels) of tick labels
**
** @see Axis#setTickLabelFontSize setTickLabelFontSize
** @see #getXAxis getXAxis
** @see #getYAxis getYAxis
** @see #getY2Axis getY2Axis
*"""
DEFAULT_TICK_LABEL_FONTSIZE = 12
"""*
** The default GWT <tt>NumberFormat</tt> format string used to convert
** numbers to the text strings displayed as tick labels
** on X, Y, and Y2 axes.
**
** @see Axis#setTickLabelFormat setTickLabelFormat
** @see #getXAxis getXAxis
** @see #getYAxis getYAxis
** @see #getY2Axis getY2Axis
**
*"""
DEFAULT_TICK_LABEL_FORMAT = "#.##"

"""*
* The default length of tick marks, in pixels.
*
* @see Axis#setTickLength setTickLength
"""
DEFAULT_TICK_LENGTH = 6


"""*
* The default tick location.
*
* @see Axis#setTickLocation setTickLocation
"""
DEFAULT_TICK_LOCATION = TickLocation.OUTSIDE


"""*
* The default thickness of tick marks, in pixels.
*
* @see Axis#setTickThickness setTickThickness
"""
DEFAULT_TICK_THICKNESS = 1; # pixel

"""*
** The default location used to position the hover feedback
** when the user hovers their mouse above a point on a curve
** that uses a VBAR_BASELINE_* symbol type.
**
** @see Symbol#setHoverLocation setHoverLocation
** @see #DEFAULT_HOVER_LOCATION DEFAULT_HOVER_LOCATION
**
"""
DEFAULT_VBAR_BASELINE_HOVER_LOCATION = AnnotationLocation.FARTHEST_FROM_HORIZONTAL_BASELINE
"""*
** The default location used to position the hover feedback
** when the user hovers their mouse above a point on a curve
** that uses a VBAR_SOUTH* symbol type.
**
** @see Symbol#setHoverLocation setHoverLocation
** @see #DEFAULT_HOVER_LOCATION DEFAULT_HOVER_LOCATION
**
"""
DEFAULT_VBARBOTTOM_HOVER_LOCATION = AnnotationLocation.NORTH

"""*
** The default location used to position the hover feedback
** when the user hovers their mouse above a point on a curve
** that uses a VBAR_NORTH* symbol type.
**
** @see Symbol#setHoverLocation setHoverLocation
** @see #DEFAULT_HOVER_LOCATION DEFAULT_HOVER_LOCATION
**
"""
DEFAULT_VBARTOP_HOVER_LOCATION = AnnotationLocation.SOUTH

"""*
** The default location used to position the
** hover feedback when the user hovers their mouse above a point
** on a curve that uses a HBAR_BASELINE_* symbol type.
**
** @see Symbol#setHoverLocation setHoverLocation
** @see #DEFAULT_HOVER_LOCATION DEFAULT_HOVER_LOCATION
**
"""
DEFAULT_HBAR_BASELINE_HOVER_LOCATION = AnnotationLocation.FARTHEST_FROM_VERTICAL_BASELINE

"""*
** The default location used to position the
** hover feedback when the user hovers their mouse above a point
** on a curve that uses an HBAR_*WEST symbol type.
**
** @see Symbol#setHoverLocation setHoverLocation
** @see #DEFAULT_HOVER_LOCATION DEFAULT_HOVER_LOCATION
**
"""
DEFAULT_HBARLEFT_HOVER_LOCATION = AnnotationLocation.EAST

"""*
** The default location used to position the
** hover feedback when the user hovers their mouse above a point
** on a curve that uses an HBAR_*EAST symbol type.
**
** @see Symbol#setHoverLocation setHoverLocation
** @see #DEFAULT_HOVER_LOCATION DEFAULT_HOVER_LOCATION
**
"""
DEFAULT_HBARRIGHT_HOVER_LOCATION = AnnotationLocation.WEST

"""*
** The default upper bound on the width of widgets used
** in annotations and tick labels that GChart
** will assume for centering and similar alignment purposes.
**
** @see Curve.Point#setAnnotationWidget setAnnotationWidget
** @see Axis#addTick(double,Widget,int,int) addTick
**
*"""
DEFAULT_WIDGET_WIDTH_UPPERBOUND = 400
"""*
** The default upper bound on the height of widgets used
** in annotations and tick labels that GChart
** will assume for centering and similar alignment purposes.
**
** @see Curve.Point#setAnnotationWidget setAnnotationWidget
** @see Axis#addTick(double,Widget,int,int) addTick
**
*"""
DEFAULT_WIDGET_HEIGHT_UPPERBOUND = 400

"""*
*  The default width of the area of the chart in
*  which curves are displayed, in pixels.
"""
DEFAULT_X_CHARTSIZE = 300; # pixels
"""*
* The default height of the area of the chart in
* which curves are displayed, in pixels.
"""
DEFAULT_Y_CHARTSIZE = 300; # pixels

"""*
** In analogy to how it uses <tt>Double.NaN</tt> (Not a
** Number), GChart uses <tt>GChart.NAI</tt> (Not an Integer) to
** represent integers whose values have not been explicitly
** specified.
**
*"""
NAI = 2L ** 31

"""*
* Due to a well-known bug (see, for example, <a
* href="http:#www.hedgerwow.com/360/dhtml/css-ie-transparent-border.html">
* this explanation on Hedger Wang's blog</a>), though white
* may not be black in IE6, transparent borders certainly are.
* Besides this outright bug, different browsers define which
* element's background color "shines through" a transparent border
* differently. For example, in FF2, the background of the element
* containing the border shines through, which makes setting the
* border color to "transparent" equivalent to setting the border
* color to equal the background color. In IE7, the color of
* the chart's background "shines through"--which is more likely
* what you intended when you set a symbol's border to transparent.
* <p>
*
* To make it easy for you to eliminate such problems, and obtain a
* consistently behaving transparent-border behavior cross-browser,
* this special GChart-only "color" (recognized by all GChart border
* color related methods <i>except</i>
* <tt>GChart.setBorderColor</tt>) causes GChart to emulate a
* transparent border by eliminating the border entirely (setting
* it's width to 0) and changing the size and position of the element
* so as to make it look like the border is still "taking up space".
*
* <p>
*
*
* <blockquote><small> <i>Note:</i>The <tt>GChart.setBorderColor</tt>
* method, which sets the color of the border around the entire
* chart, does <i>not</i> support this keyword because GChart's
* transparent border emulation relies on changing the size of, and
* shifting the position of, the transparently bordered element. But,
* the position of the GChart as a whole is determined not by GChart,
* but by the enclosing page. Well-known CSS tricks, such as
* described in the "hedgerwow" link above, can be used if you need a
* Truely transparent border around the entire chart. Or, just fake
* it by setting the border color to equal the background color
* of the containing page.  </small></blockquote>
*
* <p>
*
* This differs from setting the border color to "transparent" (which
* you can still do should you need the "standard non-standard"
* transparent border color behavior) in subtle ways that can matter
* in special cases. For example, because the element is smaller than
* it is with "transparent", if you draw your symbols outside the
* chart rectangle, GChart will not be able to track the mouse moves
* inside the transparent region (yes, this is a fine point, but
* there could be other differences I'm not aware of). In almost
* every other case I can think of, though, setting the border color
* to this special keyword instead of "transparent" will be the
* simplest way to eliminate these inconsistent transparent border
* problems from your charts.
* <p>
*
* @see Symbol#setBorderColor setBorderColor
*
"""

TRANSPARENT_BORDER_COLOR = None

"""*
** A special value used to tell GChart that a property should
** be defined via CSS, not via an explicit Java API specification.
**
**
** Note that certain CSS convenience methods that could in
** principle have been added, such as those for defining the
** background image of a chart, were omitted because I
** thought they would almost never be used. Of course, you
** can always access these CSS properties "the old fashioned
** way" (via a CSS specification or methods of the GWT DOM class).
**
** <p>
** </small></blockquote>
**
** @see #setBorderColor(String) setBorderColor
** @see #setBorderStyle(String) setBorderStyle
** @see #setBackgroundColor(String) setBackgroundColor
** @see #setBorderWidth(String) setBorderWidth
** @see #setFontFamily(String) setFontFamily
**
**
**
*"""
"""
* Setting a CSS property to "" generally clears the
* attribute specification, restoring things to their initial
* defaults (not sure if this always works, but it appears to
* so far).
*
"""
USE_CSS = ""

"""*
** Keyword used to indicate that a curve should be
** displayed on the left y-axis.
**
** @see #Y2_AXIS Y2_AXIS
** @see GChart.Curve#setYAxis(GChart.YAxisId) setYAxis
**
*"""
Y_AXIS = YAxisId()

"""*
** Keyword used to indicate that a curve should be
** displayed on the right (the so-called y2) y-axis.
**
** @see #Y_AXIS Y_AXIS
** @see Curve#setYAxis setYAxis
**
*"""
Y2_AXIS = YAxisId()

"""*
** The default URL GChart will use to access the blank image
** (specifically, a 1 x 1 pixel transparent GIF) it requires
** to prevent "missing image" icons from appearing in your
** charts.
**
** @see #setBlankImageURL setBlankImageURL
**
*"""
DEFAULT_BLANK_IMAGE_URL = "gchart.gif"
"""*
** The full path to the default GChart blank image
** (specifically, a 1 x 1 pixel transparent GIF) it requires
** to prevent "missing image" icons from appearing in your
** charts.
** <p>
**
** Convenience constant equal to:
**
** <pre>
** GWT.getModuleBaseURL()+GChart.DEFAULT_BLANK_IMAGE_URL
** </pre>
**
** @see #setBlankImageURL setBlankImageURL
**
*"""
DEFAULT_BLANK_IMAGE_URL_FULLPATH = GWT.getModuleBaseURL()+GChart.DEFAULT_BLANK_IMAGE_URL
DEFAULT_GRID_HEIGHT = DEFAULT_TICK_THICKNESS
DEFAULT_GRID_WIDTH = DEFAULT_TICK_THICKNESS
GRID_BORDER_STYLE = "solid"
GRID_BORDER_WIDTH = 1

"""* The default color used for all axes, gridlines, and ticks.
**
** @see #setGridColor setGridColor
**
"""
DEFAULT_GRID_COLOR = "black"


"""* The default thickness (height) of the rectangular region at
** the bottom of the chart allocated for footnotes, per
** <tt>&lt;br&gt;</tt> or <tt>&lt;li&gt;</tt> delimited HTML line. This
** default is only used when the footnote thickness is set to
** <tt>GChart.NAI</tt> (the default).
**
** @see #setChartFootnotesThickness setChartFootnotesThickness
**
"""
DEFAULT_FOOTNOTES_THICKNESS = 15

"""*
**
** The default thickness (height) of the rectangular region at
** the top of the chart allocated for the chart's title, per
** <tt>&lt;br&gt;</tt> or <tt>&lt;li&gt;</tt> delimited HTML line. This default
** is only used when the title thickness is set to
** <tt>GChart.NAI</tt>.
**
**
** @see #setChartTitleThickness setChartTitleThickness
**
"""
DEFAULT_TITLE_THICKNESS = 15



# for purposes of estimating fixed space "band" around the plot
# panel reserved for the tick labels:
double
TICK_CHARHEIGHT_TO_FONTSIZE_LOWERBOUND = 1.0
# a bit larger than the 0.6 rule-of-thumb
double
TICK_CHARWIDTH_TO_FONTSIZE_LOWERBOUND = 0.7
# For estimating size of invisible "box" needed for alignment
# purposes.  Note: when these are bigger, annotations remain
# properly aligned longer as user zooms up font sizes.  But,
# bigger bounding boxes can slow updates (not sure why,
# maybe it's related to hit testing browser has to do)
double
CHARHEIGHT_TO_FONTSIZE_UPPERBOUND = 2*1.5
double
CHARWIDTH_TO_FONTSIZE_UPPERBOUND = 2*0.7

TICK_BORDER_STYLE = GRID_BORDER_STYLE
TICK_BORDER_WIDTH = GRID_BORDER_WIDTH

# # of system curves "underneath" (before in DOM-order) user's curves
N_PRE_SYSTEM_CURVES = 16
# # of system curves "on top of" (after in DOM-order) user's curves
N_POST_SYSTEM_CURVES = 2
N_SYSTEM_CURVES = N_PRE_SYSTEM_CURVES+ N_POST_SYSTEM_CURVES
# index of curve that holds correspondingly-named chart part
# (sys curve indexes are negative & not directly developer-accessible)
PLOTAREA_ID = 0-N_SYSTEM_CURVES
TITLE_ID = 1-N_SYSTEM_CURVES
YAXIS_ID = 2-N_SYSTEM_CURVES
YTICKS_ID = 3-N_SYSTEM_CURVES
YGRIDLINES_ID = 4-N_SYSTEM_CURVES
YLABEL_ID = 5-N_SYSTEM_CURVES
Y2AXIS_ID = 6-N_SYSTEM_CURVES
Y2TICKS_ID = 7-N_SYSTEM_CURVES
Y2GRIDLINES_ID = 8-N_SYSTEM_CURVES
Y2LABEL_ID = 9-N_SYSTEM_CURVES
LEGEND_ID = 10-N_SYSTEM_CURVES
XAXIS_ID = 11-N_SYSTEM_CURVES
XTICKS_ID = 12-N_SYSTEM_CURVES
XGRIDLINES_ID = 13-N_SYSTEM_CURVES
XLABEL_ID = 14-N_SYSTEM_CURVES
FOOTNOTES_ID = 15-N_SYSTEM_CURVES
HOVER_CURSOR_ID = 16-N_SYSTEM_CURVES
HOVER_ANNOTATION_ID = 17-N_SYSTEM_CURVES

def setBackgroundColor(uio, cssColor):
    DOM.setStyleAttribute(uio.getElement(), "backgroundColor", cssColor)


"""
def setBackground(uio, cssColor):
    DOM.setStyleAttribute(uio.getElement(), "background", cssColor)

"""
def setBorderColor(uio, cssColor):
    DOM.setStyleAttribute(uio.getElement(), "borderColor", cssColor)





def setBorderStyle(uio, cssBorderStyle):
    DOM.setStyleAttribute(uio.getElement(), "borderStyle", cssBorderStyle)



def setBorderWidth(uio, cssBorderWidth):
    DOM.setStyleAttribute(uio.getElement(), "borderWidth", cssBorderWidth)


def setBorderWidth(uio, borderWidth):
    if borderWidth != GChart.NAI:
        setBorderWidth(uio, borderWidth + "px")
    else:
        setBorderWidth(uio, "")


def setFontFamily(uio, cssFontFamily):
    DOM.setStyleAttribute(uio.getElement(), "fontFamily", cssFontFamily)


def setFontSize(uio, fontSize):
    DOM.setIntStyleAttribute( uio.getElement(), "fontSize", fontSize)

def setFontStyle(uio, fontStyle):
    DOM.setStyleAttribute(uio.getElement(), "fontStyle", fontStyle)

def setFontWeight(uio, fontWeight):
    DOM.setStyleAttribute(uio.getElement(), "fontWeight", fontWeight)

def setColor(uio, cssColor):
    DOM.setStyleAttribute(uio.getElement(), "color", cssColor)

"""
# valid layout strings are fixed, auto, and inherit
def setTableLayout(uio, layout):
    DOM.setStyleAttribute( uio.getElement(), "table-layout", layout)




def setLineHeight(uio, cssLineHeight):
    DOM.setStyleAttribute(uio.getElement(), "lineHeight", cssLineHeight)



def setTextAlign(uio, cssTextAlign):
    DOM.setStyleAttribute( uio.getElement(), "textAlign", cssTextAlign)

def setMargin(uio, cssMargin):
    DOM.setStyleAttribute( uio.getElement(), "margin", cssMargin)

"""
def setPadding(uio, cssPadding):
    DOM.setStyleAttribute(uio.getElement(), "padding", cssPadding)

# valid choices are block, inline, list-item, or none
"""
def setDisplay(uio, cssDisplay):
    DOM.setStyleAttribute( uio.getElement(), "display", cssDisplay)

"""
# choices are: visible, hidden, scroll or auto
def setOverflow(uio, cssOverflow):
    DOM.setStyleAttribute( uio.getElement(), "overflow", cssOverflow)

"""
def setTextLeading(uio, cssTextLeading):
    DOM.setStyleAttribute( uio.getElement(), "textTrailing", cssTextLeading)

def setVerticalAlign(uio, cssVerticalAlign):
    DOM.setStyleAttribute( uio.getElement(), "verticalAlign", cssVerticalAlign)

"""
# returns the sign of the given number
def sign(self, x):
    result = (x < 0) and -1 or 1
    return result


# axis types (used to define which y-axis each curve is on)
class YAxisId(object):
    pass

# case-independent index of next "break" tag in string (case of HTML
# returned from HasHTML.getHTML can change with browser)
def indexOfBr(self, s, iStart=0):
    BR1 = "<br>"
    BR2 = "<BR>"
    BR3 = "<li>";  # recognize <li> as a break.
    BR4 = "<LI>"
    BR5 = "<tr>";  # recognize <tr> as a break.
    BR6 = "<TR>"
    iBr1 = s.indexOf(BR1, iStart)
    iBr2 = s.indexOf(BR2, iStart)
    iBr3 = s.indexOf(BR3, iStart)
    iBr4 = s.indexOf(BR4, iStart)
    iBr5 = s.indexOf(BR5, iStart)
    iBr6 = s.indexOf(BR6, iStart)
    result1 = 0
    result2 = 0
    result3 = 0
    result = 0

    if -1 == iBr1:
        result1 = iBr2

    elif -1 == iBr2:
        result1 = iBr1

    else:
        result1 = Math.min(iBr1, iBr2)


    if -1 == iBr3:
        result2 = iBr4

    elif -1 == iBr4:
        result2 = iBr3

    else:
        result2 = Math.min(iBr3, iBr4)


    if -1 == iBr5:
        result3 = iBr6

    elif -1 == iBr6:
        result3 = iBr5

    else:
        result3 = Math.min(iBr5, iBr6)




    if -1 == result1:
        result = result2

    elif -1 == result2:
        result = result1

    else:
        result = Math.min(result1, result2)



    if -1 == result:
        result = result3

    elif -1 != result3:
        result = Math.min(result, result3)



    return result


# Provides a character-based width estimate when simple tags
# such as <b> and <i> are present in a multi-line,
# "break"-delimited, string. Very approximate, but a useful
# default.
def htmlWidth(self, sIn):
    iBr = indexOfBr(sIn)
    if (-1 == iBr):
        s = sIn
    else:
        s = sIn.substring(0, iBr)
    LITERAL_PAT = "[&][#a-zA-Z]+[;]"
    s = s.replaceAll(LITERAL_PAT, "X"); # literals count as 1 char
    TAG_PAT = "[<][^>]+[>]"
    s = s.replaceAll(TAG_PAT, "");   # tags don't count at all
    return s.length()


# number of <br> delimited lines in an HTML string
def htmlHeight(self, s):
    BR_LEN = len("<br>")
    iBr = 0
    result = 1
    if None != s:
        iBr = indexOfBr(s)
        while iBr != -1:
            result += 1
            iBr = indexOfBr(s, iBr+BR_LEN)

    return result





# Validates multipliers used to simplify computing the
# upper left corner location of symbols and labels to
# properly reflect their alignment relative to the
# plotted point or labeled symbol.
def validateMultipliers(self, widthMultiplier, heightMultiplier):
    if (not (widthMultiplier == 0  or  Math.abs(widthMultiplier)==1)  and  
        not (heightMultiplier == 0  or Math.abs(heightMultiplier)==1)):
        raise IllegalArgumentException(
        "widthMultiplier, heightMultiplier args must both be " +
        "either 0, 1, or -1")



# is value within given limits, inclusive?
def withinRange(self, x, minLim, maxLim):
    # x!=x is a faster isNaN; NaN is considered in range
    result = (x!=x) and True or (x >= minLim  and  x <= maxLim)
    return result

# Is the symbol type one of the special ANCHOR_MOUSE types,
# whose position varies with the mouse cursor location?
def isMouseAnchored(symbolType):
    return (SymbolType.ANCHOR_MOUSE == symbolType  or
            SymbolType.ANCHOR_MOUSE_SNAP_TO_X == symbolType  or 
            SymbolType.ANCHOR_MOUSE_SNAP_TO_Y == symbolType)


"""*
* A GChart can represent and display a line chart, a bar chart,
* a pie chart, an area chart, or a chart that contains arbitrary
* combinations of line, bar, pie, and/or area based curves.
*
* <p>
* For detailed examples, with screen shots, visit the
* <a href="package-summary.html#ChartGallery">
* Chart Gallery</a>.
*
* <p>
* For detailed instructions on how to integrate Client-side GChart
* into your GWT application, see
* <a href="package-summary.html#InstallingGChart">
* Installing Client-side GChart</a>.
*
* <p>
* <b>CSS Style Rule</b>
* <ul>
* .gchart-GChart {the GChart's primary top-level styles }
* </ul>
*
*
* It is sometimes more natural to consider certain CSS
* attributes as properties of a GChart Java object. So, GChart
* supports "CSS convenience methods" that let you (optionally) use
* Java to specify GChart CSS attributes such as
* <tt>border-color</tt> and <tt>background-color</tt>. See
* {@link #USE_CSS USE_CSS} for a detailed description of these
* CSS convenience methods--which won't interfere with standard
* CSS-based specifications if you never invoke them.
*
*
*"""

class GChart (Composite):


    """*
    *
    * Tells GChart how to create the canvas widgets it needs
    * (specifically, widgets that implement GChart's
    * <tt>GChartCanvasLite</tt> interface) to render your
    * charts using an external vector graphics library.  <p>
    *
    * You must define a class that implements
    * <tt>GChartCanvasFactory</tt> and then pass an instance of that
    * class to this method, if you want to have the fast, crisply drawn
    * connecting lines, polygonal areas, and 2-D pie slices that only a
    * vector graphics library can provide.
    * <p>
    *
    * @see GChartCanvasFactory GChartCanvasFactory
    * @see GChartCanvasLite GChartCanvasLite
    * @see #getCanvasFactory getCanvasFactory
    * @see GChart.Symbol#setFillSpacing setFillSpacing
    * @see GChart.Symbol#setFillThickness setFillThickness
    *
    """
    def setCanvasFactory(self, factory):
        self.canvasFactory = factory


    """*
    * Returns the GChart class' canvas factory, or <tt>None</tt>
    * if no canvas factory has been specified.
    *
    * @return the previously specified canvas factory
    *
    * @see #setCanvasFactory setCanvasFactory
    *
    """
    def getCanvasFactory(self):
        return self.canvasFactory




    def getLastPieSliceOrientation(self):
        return lastPieSliceOrientation

    def setLastPieSliceOrientation(self, lastOrientation):
        lastPieSliceOrientation = lastOrientation%1.0

    """* Sets the default initial orientation for pie slices.
    **
    ** The default initial orientation is used as the first pie
    ** slice's first edge's orientation setting only if the symbol associated
    ** with that pie slice has the default, undefined, orientation
    ** setting of <tt>Double.NaN</tt>.
    ** <p>
    ** The default value of this setting is 0, which corresponds
    ** to due south (6 o'clock). The value specifies the
    ** fraction of a complete clockwise rotation, beginning
    ** at due south required to reach the first edge of the
    ** pie slice.
    **
    ** @see Symbol#setPieSliceOrientation setPieSliceOrientation
    **
    ** @param orientation the orientation to use for the first
    **   edge of the first pie slice in this GChart, in cases
    **   in which that first pie slice's orientation is undefined
    **   (<tt>Double.NaN</tt>).
    *"""

    def setInitialPieSliceOrientation(self, orientation):
        if orientation < 0  or  orientation >=1:
            raise IllegalArgumentException(
            "orientation="+orientation+"; "+
            "orientation must be >=0 and < 1.")

        self.initialPieSliceOrientation = orientation
        invalidateAllSlices()


    """*
    ** Returns a previously specified initial pie slice orientation.
    **
    ** @return the fraction of a clockwise rotation, beginning
    **   from the 6 o'clock postion, needed to reach the default
    **   initial pie slice orientation.
    **
    ** @see #setInitialPieSliceOrientation
    **   setInitialPieSliceOrientation
    *"""
    def getInitialPieSliceOrientation(self):
        return initialPieSliceOrientation









    # adds system curves GChart uses to render title, ticks, etc.
    def addSystemCurves(self):
        # Must be first: other methods assume sys curves exist
        for i in range(N_SYSTEM_CURVES):
            c = Curve(i)
            self.curves.add(c)
            # Required rendering panels are added lazily, later on


        # define (or default) properties, points on, system curves
        c = getSystemCurve(PLOTAREA_ID)
        c.getSymbol().setSymbolType(SymbolType.BOX_SOUTHEAST)
        c.getSymbol().setBackgroundColor(DEFAULT_PLOTAREA_BACKGROUND_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_PLOTAREA_BORDER_COLOR)
        c.getSymbol().setBorderStyle(DEFAULT_PLOTAREA_BORDER_STYLE)
        c.getSymbol().setBorderWidth(DEFAULT_PLOTAREA_BORDER_WIDTH)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(-Double.MAX_VALUE,Double.MAX_VALUE)

        c = getSystemCurve(TITLE_ID)
        c.getSymbol().setSymbolType(SymbolType.ANCHOR_NORTHWEST)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(0,0)
        c.getPoint().setAnnotationLocation(AnnotationLocation.CENTER)

        c = getSystemCurve(YAXIS_ID)
        c.getSymbol().setSymbolType(SymbolType.XGRIDLINE)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(GRID_BORDER_STYLE)
        c.getSymbol().setBorderWidth(GRID_BORDER_WIDTH)
        c.getSymbol().setWidth(DEFAULT_GRID_WIDTH)
        c.getSymbol().setHeight(DEFAULT_GRID_HEIGHT)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(-Double.MAX_VALUE,-Double.MAX_VALUE)

        c = getSystemCurve(YTICKS_ID)
        c.getSymbol().setSymbolType(SymbolType.BOX_WEST)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(TICK_BORDER_STYLE)
        c.getSymbol().setBorderWidth(TICK_BORDER_WIDTH)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        # points, annotation locations added when ticks are

        c = getSystemCurve(YGRIDLINES_ID)
        c.getSymbol().setSymbolType(SymbolType.YGRIDLINE)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(GRID_BORDER_STYLE)
        c.getSymbol().setBorderWidth(GRID_BORDER_WIDTH)
        c.getSymbol().setWidth(DEFAULT_GRID_WIDTH)
        c.getSymbol().setHeight(DEFAULT_GRID_HEIGHT)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)

        c = getSystemCurve(YLABEL_ID)
        c.getSymbol().setSymbolType(SymbolType.ANCHOR_WEST)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(0,0)
        c.getPoint().setAnnotationLocation(AnnotationLocation.CENTER)

        c = getSystemCurve(Y2AXIS_ID)
        c.setYAxis(Y2_AXIS)
        c.getSymbol().setSymbolType(SymbolType.XGRIDLINE)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(GRID_BORDER_STYLE)
        c.getSymbol().setBorderWidth(GRID_BORDER_WIDTH)
        c.getSymbol().setWidth(DEFAULT_GRID_WIDTH)
        c.getSymbol().setHeight(DEFAULT_GRID_HEIGHT)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(Double.MAX_VALUE,-Double.MAX_VALUE)

        c = getSystemCurve(Y2TICKS_ID)
        c.setYAxis(Y2_AXIS)
        c.getSymbol().setSymbolType(SymbolType.BOX_EAST)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(TICK_BORDER_STYLE)
        c.getSymbol().setBorderWidth(TICK_BORDER_WIDTH)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)

        c = getSystemCurve(Y2GRIDLINES_ID)
        c.setYAxis(Y2_AXIS)
        c.getSymbol().setSymbolType(SymbolType.YGRIDLINE)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(GRID_BORDER_STYLE)
        c.getSymbol().setBorderWidth(GRID_BORDER_WIDTH)
        c.getSymbol().setWidth(DEFAULT_GRID_WIDTH)
        c.getSymbol().setHeight(DEFAULT_GRID_HEIGHT)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)

        c = getSystemCurve(Y2LABEL_ID)
        c.getSymbol().setSymbolType(SymbolType.ANCHOR_EAST)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(0,0)
        c.getPoint().setAnnotationLocation(AnnotationLocation.CENTER)

        c = getSystemCurve(LEGEND_ID)
        c.getSymbol().setSymbolType(SymbolType.ANCHOR_EAST)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(0,0)
        c.getPoint().setAnnotationLocation(AnnotationLocation.CENTER)

        c = getSystemCurve(XAXIS_ID)
        c.getSymbol().setSymbolType(SymbolType.YGRIDLINE)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(GRID_BORDER_STYLE)
        c.getSymbol().setBorderWidth(GRID_BORDER_WIDTH)
        c.getSymbol().setWidth(DEFAULT_GRID_WIDTH)
        c.getSymbol().setHeight(DEFAULT_GRID_HEIGHT)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(-Double.MAX_VALUE,-Double.MAX_VALUE)

        # tick thickness and length get set in the axis constructors
        c = getSystemCurve(XTICKS_ID)
        c.getSymbol().setSymbolType(SymbolType.BOX_SOUTH)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(TICK_BORDER_STYLE)
        c.getSymbol().setBorderWidth(TICK_BORDER_WIDTH)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)

        c = getSystemCurve(XGRIDLINES_ID)
        c.getSymbol().setSymbolType(SymbolType.XGRIDLINE)
        c.getSymbol().setBackgroundColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderColor(DEFAULT_GRID_COLOR)
        c.getSymbol().setBorderStyle(GRID_BORDER_STYLE)
        c.getSymbol().setBorderWidth(GRID_BORDER_WIDTH)
        c.getSymbol().setWidth(DEFAULT_GRID_WIDTH)
        c.getSymbol().setHeight(DEFAULT_GRID_HEIGHT)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)

        c = getSystemCurve(XLABEL_ID)
        c.getSymbol().setSymbolType(SymbolType.ANCHOR_SOUTH)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(0,0)
        c.getPoint().setAnnotationLocation(AnnotationLocation.CENTER)

        c = getSystemCurve(FOOTNOTES_ID)
        c.getSymbol().setSymbolType(SymbolType.ANCHOR_SOUTHWEST)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(0,0)
        c.getPoint().setAnnotationLocation(AnnotationLocation.CENTER)

        c = getSystemCurve(HOVER_ANNOTATION_ID)
        c.setVisible(False); # initially no hover annotation
        c.getSymbol().setSymbolType(SymbolType.NONE)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(Double.NaN,Double.NaN)
        c.getPoint().setAnnotationLocation(AnnotationLocation.CENTER)

        c = getSystemCurve(HOVER_CURSOR_ID)
        c.setVisible(False); # initially no hover selection
        c.getSymbol().setSymbolType(SymbolType.NONE)
        c.getSymbol().setHoverAnnotationEnabled(False)
        c.getSymbol().setHoverSelectionEnabled(False)
        c.addPoint(Double.NaN,Double.NaN)
        c.getPoint().setAnnotationLocation(AnnotationLocation.CENTER)

        # external "curve count" should now be 0 (system curves don't count)
        if self.getNCurves() != 0:
            raise new
            IllegalStateException("self.getNCurves() != 0. Probably a GChart bug.")



    """
    * Updates the system curves that represent chart
    * decorations (axis labels, title, ticks, etc.).<p>
    *
    * Note that all x, y shifts are relative to the "anchoring"
    * symbol type locations defined once and for all in the
    * addSystemCurves method above.
    *
    """
    def updateDecorations(self, xChartSizeDecorated):


        # x-axis label
        getSystemCurve(XLABEL_ID).getPoint(0).setAnnotationWidget(
        getXAxis().getAxisLabel(), getXChartSize(),
        getXAxis().getAxisLabelThickness())
        getSystemCurve(XLABEL_ID).getPoint(0).setAnnotationYShift(
        - getXAxis().getTickLabelThickness(False)
        - getXAxis().getTickSpace()
        - getXAxis().getTickLabelPadding()
        - getXAxis().getAxisLabelThickness()/2)

        # y-axis label
        getSystemCurve(YLABEL_ID).getPoint(0).setAnnotationWidget(
        getYAxis().getAxisLabel(),
        getYAxis().getAxisLabelThickness(), getYChartSize())
        getSystemCurve(YLABEL_ID).getPoint(0).setAnnotationXShift(
        - getYAxis().getTickLabelThickness(False)
        - getYAxis().getTickSpace()
        - getYAxis().getTickLabelPadding()
        - getYAxis().getAxisLabelThickness()/2)

        # y2-axis label
        getSystemCurve(Y2LABEL_ID).getPoint(0).setAnnotationWidget(
        getY2Axis().getAxisLabel(),
        getY2Axis().getAxisLabelThickness(), getYChartSize())
        getSystemCurve(Y2LABEL_ID).getPoint(0).setAnnotationXShift(
        + getY2Axis().getTickLabelThickness(False)
        + getY2Axis().getTickSpace()
        + getY2Axis().getTickLabelPadding()
        + getY2Axis().getAxisLabelThickness()/2)

        # legend
        legend = None
        if self.isLegendVisible()  and  0 < getNVisibleCurvesOnLegend():
            legend = createLegend(self.plotPanel)

        getSystemCurve(LEGEND_ID).getPoint(0).setAnnotationWidget(
                                legend, getLegendThickness(), getYChartSize())
        getSystemCurve(LEGEND_ID).getPoint(0).setAnnotationXShift(
                                + getY2Axis().getTickLabelThickness(False)
                                + getY2Axis().getTickSpace()
                                + getY2Axis().getTickLabelPadding()
                                + getY2Axis().getAxisLabelThickness()
                                + getLegendThickness()/2 )

        # title
        shiftToLeftEdge = (- getYAxis().getAxisLabelThickness()
                           - getYAxis().getTickLabelThickness(False)
                           - getYAxis().getTickSpace()
                           - getYAxis().getTickLabelPadding())
        shiftToHorizontalMidpoint = shiftToLeftEdge + xChartSizeDecorated/2
        getSystemCurve(TITLE_ID).getPoint(0).setAnnotationWidget(
                                    getChartTitle(), xChartSizeDecorated,
                                    getChartTitleThickness())
        getSystemCurve(TITLE_ID).getPoint(0).setAnnotationYShift(
                                        getChartTitleThickness()/2)
        getSystemCurve(TITLE_ID).getPoint(0).setAnnotationXShift(
                                        shiftToHorizontalMidpoint)

        # footnotes
        getSystemCurve(FOOTNOTES_ID).getPoint(0).setAnnotationWidget(
                                    getChartFootnotes(), xChartSizeDecorated,
                                    getChartFootnotesThickness())
        getSystemCurve(FOOTNOTES_ID).getPoint(0).setAnnotationYShift(
                                    - getXAxis().getTickLabelThickness(False)
                                    - getXAxis().getTickSpace()
                                    - getXAxis().getTickLabelPadding()
                                    - getXAxis().getAxisLabelThickness()
                                    - getChartFootnotesThickness()/2 )
        if getChartFootnotesLeftJustified():
            getSystemCurve(FOOTNOTES_ID).getPoint(0).setAnnotationXShift(
                                            shiftToLeftEdge)
            getSystemCurve(FOOTNOTES_ID).getPoint(0).setAnnotationLocation(
                                            AnnotationLocation.EAST)

        else:
            # footnotes centered
            getSystemCurve(FOOTNOTES_ID).getPoint(0).setAnnotationXShift(
            shiftToHorizontalMidpoint)
            getSystemCurve(FOOTNOTES_ID).getPoint(0).setAnnotationLocation(
            AnnotationLocation.CENTER)



        # add points to ticks and gridlines curves in accord with chart specs

        # x & y axis can be present even if no curves mapped to them
        getSystemCurve(XAXIS_ID).setVisible(getXAxis().getAxisVisible())
        getXAxis().populateGridlines()
        getSystemCurve(YAXIS_ID).setVisible(getYAxis().getAxisVisible())
        getYAxis().populateGridlines()

        # y2 axis is present only if at least 1 curve is on it.
        if hasY2Axis():
            getY2Axis().populateGridlines()
            getSystemCurve(Y2AXIS_ID).setVisible(getY2Axis().getAxisVisible())
            getSystemCurve(Y2TICKS_ID).setVisible(True)
            getSystemCurve(Y2GRIDLINES_ID).setVisible(True)

        else:
            getSystemCurve(Y2AXIS_ID).setVisible(False)
            getSystemCurve(Y2TICKS_ID).setVisible(False)
            getSystemCurve(Y2GRIDLINES_ID).setVisible(False)




    """*
    * Instantiates a GChart with a curve display region of
    * the specified size.
    *
    *
    * @param xChartSize the width of the curve display region, in pixels.
    * @param yChartSize the height of the curve display region, in pixels.
    *
    * @see #setXChartSize setXChartSize
    * @see #setYChartSize setYChartSize
    * @see #setChartSize setChartSize
    """
    def __init__(self, xChartSize, yChartSize, **kwargs):

        self.hoverParameterInterpreter = None
        self.hoverTouchingEnabled = True

        self.defaultSymbolBorderColors = DEFAULT_SYMBOL_BORDER_COLORS
        # creates canvas Widgets GChart needs for *_CANVAS symbol types.
        self.canvasFactory = None

        # outer container needed so CSS-defined paddings don't interfere with positioning
        self.chartPanel = SimplePanel()

        self.borderWidth = USE_CSS
        self.borderStyle = USE_CSS
        self.borderColor = USE_CSS
        self.backgroundColor = USE_CSS
        self.blankImageURL = None
        self.chartDecorationsChanged = True
        # collection of curves associated with this chart.
        self.curves = []
        self.fontFamily = USE_CSS
        self.footnotesThickness = GChart.NAI
        self.legendBackgroundColor = DEFAULT_LEGEND_BACKGROUND_COLOR
        self.legendBorderColor = DEFAULT_LEGEND_BORDER_COLOR
        self.legendBorderWidth = DEFAULT_LEGEND_BORDER_WIDTH
        self.legendBorderStyle = DEFAULT_LEGEND_BORDER_STYLE
        self.legendThickness = GChart.NAI

        self.isLegendVisible = True

        self.legendFontColor = DEFAULT_FONT_COLOR
        self.legendFontSize = DEFAULT_LEGEND_FONTSIZE
        self.legendFontStyle = DEFAULT_FONT_STYLE
        self.legendFontWeight = DEFAULT_FONT_WEIGHT

        """
        * Contains the plotting region, as well as axes, ticks, and
        * tick-labels associated with that region. Note that tickText
        * must be centered on the ticks--placing them on the same
        * AbsolutePanel as the ticks/plots facilitates self.
        *
        """
        self.plotPanel =  PlotPanel()
        self.padding = USE_CSS
        self.optimizeForMemory = False
        self.clipToPlotArea = False
        self.clipToDecoratedChart = False
        self.titleThickness = GChart.NAI

        Composite.__init__(self, **kwargs)

        self.wasUnloaded = False
        self.addSystemCurves();  # must come first: later lines use system curves
        self.xAxis = XAxis()
        self.yAxis = YAxis()
        self.y2Axis = Y2Axis()
        self.setXChartSize(xChartSize)
        self.setYChartSize(yChartSize)
        # Note: plotPanel (where real chart resides) won't get
        # added to chartPanel (top-level do-nothing container for
        # padding and such) until AFTER first update; FF2 has some
        # serious performance problems otherwise for common usage
        # scenarios with large widget-count pages.
        self.initWidget(self.chartPanel)
        """
        * See the block comment at top of "class GChart" for a detailed
        * discussion/rational for GChart's (very minimal support) of
        * stylenames. Would like deeper support if I can ever figure out
        * how to do it without hamstringing future versions by locking
        * them into a particular implementation I might need to change
        * later on. In particular, I don't know how to provide such "deep"
        * stylenames that also work consistently with canvas-rendered
        * curves.
        """
        self.setStyleName("gchart-GChart")

    """*
    * Convenience no-arg constructor equivalent to
    * <tt>GChart(DEFAULT_X_CHARTSIZE,DEFAULT_Y_CHARTSIZE)</tt>.
    *
    * @see #GChart(int,int) GChart(int,int)
    *
    """
    def __init__(self):
        this(DEFAULT_X_CHARTSIZE, DEFAULT_Y_CHARTSIZE)



    """*
    *
    * Adds an object to handle click events on this chart, that
    * is, an object whose <tt>ClickHandler.onClick</tt> method will be
    * called whenever the user clicks on this chart.
    *
    * <p>
    *
    * When implementing a class that handles GChart click
    * events, you'll need to know the following facts:
    * <p>
    *
    * <ol>
    *
    *  <li>You can use the <tt>getSource</tt> method of the
    *  <tt>ClickEvent</tt> passed into your <tt>onClick</tt> handler
    *  to retrieve the <tt>GChart</tt> that was
    *  clicked on. For example:
    *  <p>
    *
    *  <pre>
    *    # Deletes the clicked-on curve
    def onClick(self, event):
        GChart theGChart = (GChart) event.getSource()
        GChart.Curve c = theGChart.getTouchedCurve()
        if None != c:
            theGChart.removeCurve(c)
            # what you see in browser won't change without an update
            theGChart.update()


    *  </pre>
    *  <p>
    *
    *  <li>The <tt>GChart</tt> methods <tt>getTouchedPoint</tt> and
    *  <tt>getTouchedCurve</tt> return either the point and
    *  curve that were clicked on, or <tt>None</tt> if the
    *  click didn't "touch" any points.
    *
    *  <p>
    *
    *</ol>
    * <p>
    *
    * The editable pie chart example on the GChart <a
    * href="http:#gchart.googlecode.com/svn/trunk/live-demo/v2_6/com.googlecode.gchart.gchartdemoapp.GChartDemoApp/GChartDemoApp.html">
    * live demo page</a>
    * illustrates how to use this method to launch a popup modal
    * <tt>DialogBox</tt> whenever the user clicks on a point, and how to
    * change the selected point from within that dialog by using
    * GChart's <tt>touch</tt> method.
    * <p>
    *
    * For a much simpler example that lets the user
    * delete points by clicking on them, see the Chart Gallery's
    * <a href="package-summary.html#GChartExample18a">
    *  GChartExample18a</a>.
    * <p>
    *
    * @param handler the click handler that will handle
    *   click events on this chart.
    *
    * @return the handler's registration object. You need to retain a
    * reference to this registration object only if you may later need
    * to remove the handler (via the registration's
    * <tt>removeHandler</tt> method).  Most applications don't remove
    * handlers (handlers tend to be statically defined) and so can
    * ignore the value returned from this method.
    *
    * @see #getTouchedPoint getTouchedPoint
    * @see #getTouchedCurve getTouchedCurve
    * @see #touch touch
    * @see #isUpdateNeeded isUpdateNeeded
    """

    def addClickHandler(self, handler):
        result = addDomHandler(handler, ClickEvent.getType())
        return result


    def addDoubleClickHandler(self, handler):
        result = addDomHandler(handler, DoubleClickEvent.getType())
        return result



    def addMouseDownHandler(self, handler):
        result = addDomHandler(handler, MouseDownEvent.getType())
        return result

    def addMouseMoveHandler(self, handler):
        result = addDomHandler(handler, MouseMoveEvent.getType())
        return result

    def addMouseOutHandler(self, handler):
        result = addDomHandler(handler, MouseOutEvent.getType())
        return result

    def addMouseOverHandler(self, handler):
        result = addDomHandler(handler, MouseOverEvent.getType())
        return result

    def addMouseUpHandler(self, handler):
        result = addDomHandler(handler, MouseUpEvent.getType())
        return result

    def addMouseWheelHandler(self, handler):
        result = addDomHandler(handler, MouseWheelEvent.getType())
        return result


    """*
    * Adds a curve to the chart, at the end of the current
    * list of curves.
    * <p>
    *
    * @see #getCurve getCurve
    * @see #addCurve(int) addCurve(int)
    * @see #removeCurve removeCurve
    * @see #clearCurves clearCurves
    * @see #getNCurves getNCurves
    """

    def addCurve(self):
        addCurve(self.getNCurves())

    """
    * Given external, coded, index returns a curve's ArrayList index
    *
    * Basic order within the curves array is as follows:
    *
    *   o 6 decorative curves that hold title, etc
    *   o "self.getNCurves()" user-created curves
    *   o 1 "Pop-up" hover annotation holding curve
    *   o 1 Selection cursor holding curve
    *
    * It's very important that the last two system curves come last, both
    * for performance (at the end means GChart's algorithms are able to
    * update only these curves when hover feedback changes) and to
    * ensure these elements are always on top of all other chart
    * elements, as required.
    * <p>
    *
    * The "external" system curve indexes are in a continuous range of
    * negative integers, which are mapped into the ArrayList
    * positions above via this code.
    *
    """
    def internalCurveIndex(self, externalIndex):
        result
        if GChart.NAI == externalIndex:
            # -1 is the "no such curve" index used by an ArrayList
            result = -1

        elif externalIndex < -N_POST_SYSTEM_CURVES:
            # decoration related sys curves (before user's)
            result = externalIndex + N_SYSTEM_CURVES

        elif externalIndex < 0:
            # hover feedback related, after user curves (at the end)
            result = len(self.curves)+externalIndex

        else:
            # + indexes mapped to ordinary user-created curves
            result = externalIndex + N_PRE_SYSTEM_CURVES

        return result


    """ Given a curves ArrayList index returns external, coded, index
    *
    * Companion/inverse of preceeding method.
    *
    """
    def externalCurveIndex(self, internalIndex):
        result
        if internalIndex < 0:
            result = GChart.NAI

        elif internalIndex < N_PRE_SYSTEM_CURVES:
            # one of the sys curves that comes before user's curves
            result = internalIndex - N_SYSTEM_CURVES

        elif internalIndex >= len(self.curves)-N_POST_SYSTEM_CURVES:
            # sys curves, like hover feedback, that come after user's
            result =  internalIndex - len(self.curves)

        else:
            # ordinary user created curve
            result = internalIndex - N_PRE_SYSTEM_CURVES

        return result

    # does the external curve index represent a GChart-sys-defined curve?
    def isSystemCurveIndex(self, externalIndex):
        result = externalIndex < 0
        return result

    """*
    * Adds a curve to the chart, at the specified position
    * in the curve sequence. Existing curves at postions at
    * or greater than the specified position have their
    * positional indexes increased by 1.
    * <p>
    *
    * @see #getCurve getCurve
    * @see #addCurve() addCurve()
    * @see #removeCurve removeCurve
    * @see #clearCurves clearCurves
    * @see #getNCurves getNCurves
    """

    def addCurve(self, iCurve):
        if iCurve > self.getNCurves():
            raise IllegalArgumentException(
            "iCurve = " + iCurve +"; iCurve may not exceed self.getNCurves() (" + self.getNCurves() + ")")

        elif iCurve < 0:
            raise IllegalArgumentException(
            "iCurve = " + iCurve +"; iCurve may not be negative.")

        internalIndex = internalCurveIndex(iCurve)
        c = Curve(internalIndex)
        self.curves.add(internalIndex, c)
        # curves are initially added to the x, y axes.
        getXAxis().incrementCurves()
        getYAxis().incrementCurves()
        # adjust ArrayList indexes to account for newly added element
        for i in range(internalIndex+1, len(self.curves)):
            self.curves.get(i).incrementIndex()

        if 0 != self.plotPanel.getRenderingPanelCount():
            # other panels are already there
            rpIndex = getRenderingPanelIndex(internalIndex)
            self.plotPanel.addGraphicsRenderingPanel(rpIndex)
            self.plotPanel.addAnnotationRenderingPanel(rpIndex)

        # otherwise, before 1st update: lazy-add panels when they're 1st used
        c.invalidate()
        if self.getNCurves() > 0:
            setDefaultBorderColor(c, self.getNCurves()-1)




    """*
    * Removes every curve this chart contains.
    *
    * @see #getCurve getCurve
    * @see #addCurve() addCurve()
    * @see #addCurve(int) addCurve(int)
    * @see #removeCurve removeCurve
    * @see #getNCurves getNCurves
    """
    def clearCurves(self):
        for iCurve in range( self.getNCurves()-1, -1, -1):
            self.removeCurve(iCurve)


    """*
    ** Returns the background color of the chart as a whole.
    **
    ** @return the chart's background color, in a standard
    **   CSS color string format.
    **
    ** @see #setBackgroundColor(String) setBackgroundColor
    **
    *"""
    def getBackgroundColor(self):
        return(self.backgroundColor)

    """*
    ** Returns the color of the border around the chart as
    ** a whole.
    **
    ** @return the color of the chart's border, in a standard
    **   CSS color string format.
    **
    ** @see #setBorderColor(String) setBorderColor
    **
    *"""
    def getBorderColor(self):
        return self.borderColor


    """*
    ** Returns the width of the border around the chart as a whole
    **
    ** @return width of the border around the chart as a whole, as
    **   a CSS border width specification string (e.g. "1px").
    **
    ** @see #setBorderWidth(String) setBorderWidth
    **
    *"""
    def getBorderWidth(self):
        return self.borderWidth


    """*
    ** Returns the style of the border around the chart as a whole
    **
    ** @return cssStyle for the border around the chart as a whole
    **
    ** @see #setBorderStyle(String) setBorderStyle
    **
    *"""
    def getBorderStyle(self):
        return self.borderStyle



    """* Returns the previously specified chart footnotes widget.
    *
    * @return widget representing chart's footnotes or <tt>None</tt> if none.
    *
    * @see #setChartFootnotes(Widget) setChartFootnotes(Widget)
    * @see #setChartFootnotes(String) setChartFootnotes(String)
    * @see #getChartTitle getChartTitle
    """
    def getChartFootnotes(self):
        return chartFootnotes

    """* Returns flag indicating if this chart's footnotes are
    *  left-justified or centered.
    *
    * @return True if footnotes are flush against the left edge
    * of the chart, False if they are horizontally centered
    * across the bottom edge of the chart.
    *
    * @see #setChartFootnotesLeftJustified setChartFootnotesLeftJustified
    * @see #setChartFootnotes(String) setChartFootnotes(String)
    * @see #setChartTitle setChartTitle
    """
    def getChartFootnotesLeftJustified(self):
        return chartFootnotesLeftJustified

    """* Returns the thickness (height) of the rectangular region
    ** at the bottom of the chart allocated for footnotes.
    ** <p>
    **
    ** The width of this region always equals the width of
    ** the entire GChart (including legend and axis labels).
    ** <p>
    **
    ** Your footnotes widget is always vertically centered
    ** in this region.
    ** <p>
    **
    **
    ** Your footnotes widget will either be horizontally
    ** centered in this region, or left justified in it,
    ** depending on the property defined by the
    ** <tt>setChartFootnotesLeftJustified</tt> method.
    **
    ** <p>
    **
    **
    ** This method always returns 0 if the footnotes widget
    ** is <tt>None</tt> (the default); the rectangular
    ** footnotes region is entirely eliminated in that case.
    ** <p>
    **
    ** @return the thickness (height) of the rectangular region
    ** at the bottom of the chart allocated for footnotes, in
    ** pixels.
    **
    ** @see #setChartFootnotesThickness(int) setChartFootnotesThickness
    ** @see #setChartFootnotesLeftJustified setChartFootnotesLeftJustified
    *"""
    def getChartFootnotesThickness(self):
        result = 0
        EXTRA_HEIGHT = 3; # 1.5 lines padding above/below
        DEF_HEIGHT = 1
        if None == getChartFootnotes():
            result = 0

        elif GChart.NAI != self.footnotesThickness:
            result = self.footnotesThickness

        elif hasattr(getChartFootnotes(), 'getHTML'):
            result = DEFAULT_FOOTNOTES_THICKNESS * (EXTRA_HEIGHT +
                        htmlHeight( getChartFootnotes().getHTML()) )

        else:
            result = DEFAULT_FOOTNOTES_THICKNESS* (DEF_HEIGHT + EXTRA_HEIGHT)

        return result

    """* Returns the previously specified widget representing the
    *  chart's title.
    *
    * @return widget representing chart's title or <tt>None</tt>
    * if none
    *
    * @see #setChartTitle(Widget) setChartTitle(Widget)
    * @see #setChartTitle(String) setChartTitle(String)
    *
    """
    def getChartTitle(self):
        return self.chartTitle


    """*
    ** Returns the thickness (height) of the rectangular region at
    ** the top of the chart allocated for the title.
    ** <p>
    **
    ** This method always returns 0 if the title widget
    ** is <tt>None</tt> (the default); the rectangular
    ** title region is entirely eliminated in that case.
    ** <p>
    **
    ** Your title widget is always centered vertically and
    ** horizontally within this rectangular region.
    **
    **
    ** @return the thickness (height) of the rectangle
    ** that contains the chart's title, in pixels.
    **
    ** @see #setChartTitleThickness setChartTitleThickness
    **
    *"""
    def getChartTitleThickness(self):
        result = 0
        EXTRA_HEIGHT = 3; # 1.5 lines above & below title
        DEF_HEIGHT = 1
        if None == getChartTitle():
            result = 0

        elif GChart.NAI != self.titleThickness:
            result = self.titleThickness

        elif hasattr(getChartTitle(), 'getHTML'):
            result = DEFAULT_TITLE_THICKNESS * (EXTRA_HEIGHT +
                    htmlHeight( getChartTitle().getHTML() ))

        else:
            result = DEFAULT_TITLE_THICKNESS* (EXTRA_HEIGHT + DEF_HEIGHT)

        return result


    """*
    * Determines if this chart will clip any chart elements
    * that extend beyond the bounds of the decorated chart.
    * The decorated chart includes title, footnotes, etc.
    * as well as the plot area proper.
    *
    * @return True if off-the-decorated-chart elements are
    * clipped, False otherwise.
    *
    * @see #setClipToDecoratedChart setClipToDecoratedChart
    * @see #setClipToPlotArea setClipToPlotArea
    * @see #getXChartSizeDecorated getXChartSizeDecorated
    * @see #getYChartSizeDecorated getYChartSizeDecorated
    *
    """
    def getClipToDecoratedChart(self):
        return self.clipToDecoratedChart


    """*
    * Returns True if graphical aspects of the
    * chart that fall outside of the plot area are being clipped
    * off, False otherwise.
    *
    * @return <tt>True</tt> if clipping to plot area, else
    * <tt>False</tt>.
    *
    * @see #setClipToPlotArea setClipToPlotArea
    """

    def getClipToPlotArea(self):
        return self.clipToPlotArea


    # returns point closest to given plot-panel pixel coordinates
    def getClosestBrushTouchingPointNoCheck(self, x, y):

        result = None
        # NAI means mouse is at some unknown, off-the-chart, position
        if x == GChart.NAI  or  y == GChart.NAI:
            return result

        dBest = Double.MAX_VALUE; # dist. to closest symbol

        # fact that charts tend to have a small number of curves
        # allows us to use simple sequential search across curves
        nCurves = self.getNCurves()
        for iCurve in range(nCurves):
            c = getSystemCurve(iCurve)
            if not c.isVisible():
                continue

            sym = c.getSymbol()
            if not sym.getHoverAnnotationEnabled()  and  not sym.getHoverSelectionEnabled():
                continue

            symType = sym.getSymbolType()
            onY2 = c.onY2()
            iClosest = c.getClosestTouchingPoint(x, y)
            if GChart.NAI == iClosest:
                continue; # no hits on this curve


            xPoint = symType.getCenterX(self.plotPanel, sym, iClosest)
            yPoint = symType.getCenterY(self.plotPanel, sym, iClosest, onY2)
            dx = sym.xScaleFactor*(x-xPoint)
            dy = sym.yScaleFactor*(y-yPoint)
            # distance, squared, of mouse from symbol's "center"
            d = dx*dx+dy*dy
            if d <= dBest:
                # for ties, use later, "on top", point
                dBest = d
                result = c.getPoint(iClosest)


        return result

    """*
    *
    * Returns the point that would be touched if the mouse were
    * moved to the given x,y plot-area pixel coordinates, or
    * <tt>None</tt> if the moving the mouse to these coordinates
    * would not have touched any points.<p>
    *
    * This method only works if the chart rendering is
    * up-to-date (if <tt>isUpdateNeeded</tt> returns
    * <tt>False</tt>). Otherwise, <tt>None</tt> is returned.
    * <p>
    *
    * <small> GChart's hit testing method works best if a
    * chart's points are approximately evenly distributed across
    * the plot area's x or y axis, across a small number of
    * curves. In particular, charts that have many points
    * bunched up into a small part of the plot area, or that
    * have many points completely outside of the plot area, or
    * that place each point into a separate curve, could
    * experience significantly worse that usual hit testing
    * performance. Though such cases are expected to be rare, in
    * the worst case, GChart could be reduced to a simple linear
    * search across all the chart's points during hit testing.
    * </small>
    *
    * @param xPlotArea x-coordinate of trial mouse position, in
    * GChart's plot area pixel coordinates.
    * @param yPlotArea y-coordinate of trial mouse position, in
    * GChart's plot area pixel coordinates.
    *
    * @return reference to the point that would have been "touched"
    *   by the mouse, or <tt>None</tt> if positioning the mouse
    *   to these coordinates would not have touched any point.
    *
    * @see Axis#getMouseCoordinate getMouseCoordinate
    * @see Axis#modelToPlotAreaPixel modelToPlotAreaPixel
    * @see #isUpdateNeeded isUpdateNeeded
    * @see #touch touch
    *
    """

    def getClosestBrushTouchingPoint(self, xPlotArea, yPlotArea):
        result = None
        if not isUpdateNeeded():
            result = getClosestBrushTouchingPointNoCheck(xPlotArea, yPlotArea)

        return result


    """* Convenience method equivalent to <tt>getCurve(self.getNCurves()-1)</tt>.
    *  <p>
    *  This method, when used in conjunction with no-arg <tt>addCurve</tt>,
    *  method, makes code blocks that create and define the
    *  properties of a chart's curves more readable/editable. For example:
    <pre>
    addCurve(); # add 1st curve
    getCurve().setYAxis(Y2_AXIS); # first setting for 1st curve
    #... other settings for first curve
    addCurve(); # add 2nd curve
    getCurve().setYAxis(Y_AXIS); # first setting for 2nd curve
    # ... other settings for 2nd curve
    </pre>
    *<p>
    * Note that using the no-arg methods in this way allows you to copy
    * entire groups of curve properties, unchanged, between such curve
    * related blocks.
    *
    *  @return the curve with the highest integer index. In other words,
    *    the curve with an index of <tt>self.getNCurves()-1</tt>.
    *
    *  @see #getCurve(int) getCurve(int)
    *  @see #getNCurves getNCurves
    *  @see #addCurve() addCurve()
    """
    def getCurve(self):
        N = self.getNCurves()
        if N < 1:
            raise IllegalStateException(
            "You must add at least 1 curve before invoking getCurve()")

        result = getSystemCurve(N-1)
        return result


    """*
    * Returns a reference to the curve at the specified
    * positional index.  Use the reference returned by this method to
    * modify properties of a curve (the symbol, data points, etc.)
    *
    * <p>
    * @param iCurve index of the curve to be retrieved.
    * @return reference to the Curve at the specified position.
    *
    * @see #getCurve() getCurve()
    * @see #addCurve() addCurve()
    * @see #addCurve(int) addCurve(int)
    * @see #removeCurve removeCurve
    * @see #clearCurves clearCurves
    * @see #getNCurves getNCurves
    """
    def getCurve(self, iCurve):

        if iCurve >= self.getNCurves():
            raise IllegalArgumentException(
            "iCurve = " + iCurve +"; iCurve may not exceed self.getNCurves()-1 (" + (self.getNCurves()-1) + ")")

        elif iCurve < 0:
            raise IllegalArgumentException(
            "iCurve = " + iCurve +"; iCurve may not be negative.")

        result = getSystemCurve(iCurve)
        return result


    # Version of getCurve that allows sys curve (negative id) access
    def getSystemCurve(self, iCurve):
        internalIndex = internalCurveIndex(iCurve)
        result = self.curves.get(internalIndex)
        return result


    """*
    * Returns the positional index (within this chart's list of
    * curves) of the specified curve.
    * <p>
    *
    * Returns <i>GChart.NAI</i> if the specified curve is not found on
    * this GChart's curve list.
    *
    * <p>
    * @param curve whose list position is to be retrieved
    * @return position of curve in GChart's curve list, or
    *        <i>GChart.NAI</i> if not on this chart's curve list.
    *
    * @see #getCurve() getCurve()
    * @see #getCurve(int) getCurve(int)
    * @see #addCurve() addCurve()
    * @see #addCurve(int) addCurve(int)
    * @see #removeCurve removeCurve
    * @see #clearCurves clearCurves
    * @see #getNCurves getNCurves
    """
    def getCurveIndex(self, curve):
        internalIndex = curve.getIndexOf()
        result = externalCurveIndex(internalIndex)
        return result

    def getInternalCurveIndex(self, curve):
        result = curve.getIndexOf()
        return result

    # maps all background curve indexes into first rendering panel
    def getRenderingPanelIndex(self, internalCurveIndex):
        result = 0
        if N_PRE_SYSTEM_CURVES <= internalCurveIndex:
            result = internalCurveIndex - N_PRE_SYSTEM_CURVES + 1

        return result



    """* Returns the font-family used in tick labels, point annotations,
    ** legends, and as the default in titles, footnotes, and
    ** axis labels.
    **
    ** @see #setFontFamily(String) setFontFamily
    **
    **
    *"""
    def getFontFamily(self):
        return self.fontFamily


    """*
    ** Returns CSS color specification for all gridlines, axes,
    **   and tickmarks.
    **
    ** @see #setGridColor setGridColor
    **
    ** @return the color, in CSS standard color format,
    **    used for all gridlines, axes, and tick marks.
    **
    *"""

    def getGridColor(self):
        cGridlines = getSystemCurve(XGRIDLINES_ID)
        result = cGridlines.getSymbol().getBorderColor()
        return result



    """*
    ** Returns the background color of the chart's legend.
    **
    ** @return the legend's background color, in a standard
    **   CSS color string format.
    **
    ** @see #setLegendBackgroundColor setLegendBackgroundColor
    **
    *"""
    def getLegendBackgroundColor(self):
        return self.legendBackgroundColor

    """*
    ** Returns the border color of the chart's legend.
    **
    ** @return the color of the legend's border, in a standard
    **   CSS color string format, or else the special GChart keyword
    **   <tt>TRANSPARENT_BORDER_COLOR</tt>.
    **
    ** @see #setLegendBorderColor setLegendBordergroundColor
    ** @see #TRANSPARENT_BORDER_COLOR TRANSPARENT_BORDER_COLOR
    **
    *"""
    def getLegendBorderColor(self):
        return self.legendBorderColor


    """*
    ** Returns the width of the chart's legend's border
    **
    ** @return width of the legend's border, in pixels
    **
    ** @see #setLegendBorderWidth setLegendBorderWidth
    **
    *"""
    def getLegendBorderWidth(self):
        return self.legendBorderWidth


    """*
    ** Returns the style of the chart's legend's border
    **
    ** @return cssStyle of the legend's border
    **
    ** @see #setLegendBorderStyle setLegendBorderStyle
    **
    *"""
    def getLegendBorderStyle(self):
        return self.legendBorderStyle


    """*
    ** Returns the color of the font used to display the labels
    **   within the legend (chart key)
    **
    ** @return CSS color string defining the legend text's color
    **
    ** @see #setLegendFontColor setLegendFontColor
    *"""
    def getLegendFontColor(self):
        return self.legendFontColor

    """*
    * Returns the CSS font size, in pixels, of text displayed
    * in the chart's legend (also know as a chart's key).
    *
    * @return the (previously specified) font size of legend text
    *
    * @see #setLegendFontSize setLegendFontSize
    """
    def getLegendFontSize(self):
        return self.legendFontSize

    """*
    ** Returns the font-style in which this GChart's legend text
    ** will be rendered.
    **
    ** @return font-style of legend text (italic, normal, etc.)
    **
    ** @see #setLegendFontStyle setLegendFontStyle
    *"""
    def getLegendFontStyle(self):
        return self.legendFontStyle

    """*
    ** Returns True if legend text will be rendered in a bold,
    ** or False if in normal, weight font.
    **
    ** @return if the legend's text is in bold or not.
    **
    ** @see #setLegendFontWeight setLegendFontWeight
    *"""
    def getLegendFontWeight(self):
        return self.legendFontWeight

    """*
    ** Returns the thickness (width) of the rectangular region
    ** to the right of the y2-axis label allocated for the
    ** chart legend.<p>
    **
    ** The region extends vertically in parallel with the
    ** right edge of the plot area. The legend is always
    ** centered vertically and horizontally within this
    ** rectangular region.
    ** <p>
    **
    ** This method always returns 0 if the legend is not
    ** visible; the rectangular legend region is entirely
    ** eliminated in that case.
    **
    ** @return thickness (width) of legend key holding region,
    ** in pixels.
    **
    ** @see #setLegendThickness setLegendThickness
    *"""
    def getLegendThickness(self):
        result = 0
        if self.isLegendVisible()  and  0 < getNVisibleCurvesOnLegend():
            if GChart.NAI == self.legendThickness:
                result = getDefaultLegendThickness()

            else:
                result = self.legendThickness



        return result


    """*
    * Returns the number of curves on this chart.
    *
    * @return the number of curves on this chart
    *
    * @see #getCurve getCurve
    * @see #addCurve() addCurve()
    * @see #addCurve(int) addCurve(int)
    * @see #removeCurve removeCurve
    * @see #clearCurves clearCurves
    """
    def getNCurves(self):
        return len(self.curves) - N_SYSTEM_CURVES

    """* Returns the CSS string that specifies the width of the
    ** padding between the chart and it's external border
    ** <p>
    **
    ** @return the CSS string that defines the CSS padding property
    **   for the GChart as a whole.
    **
    ** @see #setPadding(String) setPadding
    **
    *"""
    def getPadding(self):
        return self.padding


    """*
    ** Returns the background color of the area of the chart
    ** in which symbols representing curve data are displayed
    **
    ** @return CSS color string defining the plot area's background
    **    color
    **
    ** @see #setPlotAreaBackgroundColor setPlotAreaBackgroundColor
    *"""
    def getPlotAreaBackgroundColor(self):
        c = getSystemCurve(PLOTAREA_ID)
        result = c.getSymbol().getBackgroundColor()
        return result


    """*
    ** Returns the border color of the area of the chart
    ** in which symbols representing curve data are displayed
    **
    ** @return CSS color string defining the color of the plot
    **    area's border
    **
    ** @see #setPlotAreaBorderColor setPlotAreaBorderColor
    *"""
    def getPlotAreaBorderColor(self):
        c = getSystemCurve(PLOTAREA_ID)
        result = c.getSymbol().getBorderColor()
        return result

    """*
    ** Returns the width of the border around the area of the
    ** chart in which symbols representing curve data are
    ** displayed.
    **
    ** @return width, in pixels, of the border around the plot area
    **
    ** @see #setPlotAreaBorderWidth setPlotAreaBorderWidth
    *"""
    def getPlotAreaBorderWidth(self):
        c = getSystemCurve(PLOTAREA_ID)
        result = c.getSymbol().getBorderWidth()
        return result


    """*
    ** Returns the style of the border around the area of the
    ** chart in which symbols representing curve data are
    ** displayed (the so-called plot area).
    **
    ** @return CSS style of the border around the plot area
    **
    ** @see #setPlotAreaBorderStyle setPlotAreaBorderStyle
    *"""
    def getPlotAreaBorderStyle(self):
        c = getSystemCurve(PLOTAREA_ID)
        result = c.getSymbol().getBorderStyle()
        return result

    """*
    *
    * Returns the image URL that will be used to define the
    * plot area's background the next time <tt>update</tt> is called.
    * <p>
    *
    * @return url of image to be used as the background of the plot
    * area the next time that <tt>update</tt> is called.
    *
    * @see #setPlotAreaImageURL setPlotAreaImageURL
    * @see #update update
    *
    """
    def getPlotAreaImageURL(self):
        c = getSystemCurve(PLOTAREA_ID)
        result = c.getSymbol().getImageURL()
        return result

    """*
    *
    * Returns a flag that tells if GChart is configured to
    * perform updates so that the chart uses less memory.
    *
    * @return <tt>True</tt> if GChart optimizes updates to
    * save memory, <tt>False</tt> (the default) if it optimizes
    * them to save time.
    *
    * @see #setOptimizeForMemory setOptimizeForMemory
    *
    *"""
    def getOptimizeForMemory(self):
        return self.optimizeForMemory



    """*
    * @deprecated
    *
    * Equivalent to <tt>!getClipToPlotArea()</tt>. Use that
    * method instead.
    *
    * @see #getClipToPlotArea getClipToPlotArea
    """

    def getShowOffChartPoints(self):
        return not getClipToPlotArea()



    """* @deprecated
    **
    ** Equivalent to <tt>!getClipToDecoratedChart()</tt>. Use
    ** that method instead.
    **
    ** @see #getClipToDecoratedChart getClipToDecoratedChart
    **
    *"""
    def getShowOffDecoratedChartGlyphs(self):
        return not getClipToDecoratedChart()



    """*
    ** Returns a URL that points to a 1 x 1 pixel blank image
    ** file GChart requires to render its charts without
    ** producing missing image icons.
    **
    ** <p>
    **
    ** @return the URL of the file GChart needs to prevent
    ** missing image icons from appearing on your chart.
    **
    ** @see #setBlankImageURL setBlankImageURL
    **
    *"""

    def getBlankImageURL(self):
        if self.blankImageURL:
            return self.blankImageURL
        return DEFAULT_BLANK_IMAGE_URL_FULLPATH


    """*
    * Returns this GChart's hover parameter interpreter.
    *
    * @see #setHoverParameterInterpreter setHoverParameterInterpreter
    *
    * @return the hover parameter interpreter used by this
    * GChart, or <tt>None</tt> if none.
    *
    """
    def getHoverParameterInterpreter(self):
        return self.hoverParameterInterpreter


    """*
    * Is it possible to select points and have their hover
    * annotations pop up, merely by "touching" them with
    * the mouse-attached "brush"?
    *
    * @return True (the default) if just hovering over a point can
    * select it, False if you must click on a point to select it.
    *
    * @see #setHoverTouchingEnabled setHoverTouchingEnabled
    *
    """
    def getHoverTouchingEnabled(self):
        return self.hoverTouchingEnabled

    """*
    * Returns the x-axis associated with this chart. Use the
    * returned reference to manipulate axis min and max,
    * number of ticks, tick positions, tick label formats, etc.
    * <p>
    * @return object representing the x-axis of this chart.
    *
    * @see #getYAxis getYAxis
    * @see #getY2Axis getY2Axis
    """
    def getXAxis(self):
        return xAxis


    """*
    * Returns the number of x-pixels in the region of the chart
    * used for curve display purposes.
    *
    * @return the number of x-pixels available for curve display.
    *
    * @see #setXChartSize setXChartSize
    *
    """
    def getXChartSize(self):
        return xChartSize


    """*
    * Returns the number of x-pixels reserved for the chart as a
    * whole, including space reserved for decorations (title,
    * footnotes, axis labels, ticks, tick labels, legend key,
    * etc.).
    * <p>
    *
    * The returned size does not include the border or padding
    * around the chart as a whole. <p>
    *
    * You cannot directly set the decorated x chart size.
    * Instead, you must set the width of the plot area, and the
    * thicknesses of certain of the decoration-holding regions
    * (using methods linked to below) that, summed together,
    * define the total width of the chart.
    *
    * @return the width of the entire chart, in pixels.
    *
    * @see #setXChartSize setXChartSize
    * @see #getYChartSizeDecorated getYChartSizeDecorated
    * @see Axis#setAxisLabelThickness setAxisLabelThickness
    * @see Axis#setTickLabelThickness setTickLabelThickness
    * @see Axis#setTickLength setTickLength
    * @see Axis#setTickLocation setTickLocation
    * @see Axis#setTickLabelPadding setTickLabelPadding
    * @see Axis#setLegendThickness setLegendThickness
    *
    """
    def getXChartSizeDecorated(self):
        result = (getXChartSize() +
                    getYAxis().getAxisLabelThickness() +
                    getYAxis().getTickLabelThickness() +
                    getYAxis().getTickSpace() +
                    getYAxis().getTickLabelPadding() +
                    getY2Axis().getAxisLabelThickness() +
                    getY2Axis().getTickLabelThickness() +
                    getY2Axis().getTickSpace() +
                    getYAxis().getTickLabelPadding() +
                    getLegendThickness())
        return result





    """*
    * Returns the y2-axis (right y axis) associated with this
    * chart. Use the returned reference to manipulate axis
    * min and max, number of ticks, tick positions, tick
    * label formats, etc.
    *
    * <p>
    * @return object representing the y2-axis of this chart.
    *
    * @see #getYAxis getYAxis
    * @see #getXAxis getXAxis
    """
    def getY2Axis(self):
        return y2Axis

    """*
    * Returns the (left) y-axis associated with this chart. Use the
    * returned reference to manipulate axis min and max,
    * number of ticks, tick positions, tick label formats, etc.
    * <p>
    * @return object representing the y-axis of this chart.
    *
    * @see #getXAxis getXAxis
    * @see #getY2Axis getY2Axis
    """
    def getYAxis(self):
        return yAxis

    """*
    * Returns the number of y-pixels in the region of the chart
    * used for curve display purposes.
    *
    * @return the number of y-pixels available for curve display.
    *
    * @see #setYChartSize setYChartSize
    *
    """
    def getYChartSize(self):
        return yChartSize


    """*
    * Returns the number of y-pixels reserved for the chart as a
    * whole, including space reserved for decorations (title,
    * footnotes, axis labels, ticks, tick labels, etc.).  <p>
    *
    * The returned size does not include the border or padding
    * around the chart as a whole. <p>
    *
    * You cannot directly set the decorated y chart size.
    * Instead, you must set sizes and thicknesses of the
    * plot area and certain of the decoration-holding regions
    * (using the methods linked-to below) that, when summed
    * together, define the height of the decorated chart.
    *
    * @return the height of the entire chart, in pixels.
    *
    * @see #setYChartSize setYChartSize
    * @see #getXChartSizeDecorated getXChartSizeDecorated
    * @see Axis#setAxisLabelThickness setAxisLabelThickness
    * @see Axis#setTickLabelThickness setTickLabelThickness
    * @see Axis#setTickLength setTickLength
    * @see Axis#setTickLocation setTickLocation
    * @see Axis#setTickLabelPadding setTickLabelPadding
    * @see #setChartTitleThickness setChartTitleThickness
    * @see #setChartFootnotesThickness setChartFootnotesThickness
    *
    """
    def getYChartSizeDecorated(self):
        result = (getYChartSize() +
                    getXAxis().getAxisLabelThickness() +
                    getXAxis().getTickLabelThickness() +
                    getXAxis().getTickSpace() +
                    getXAxis().getTickLabelPadding() +
                    getChartTitleThickness() +
                    getChartFootnotesThickness())

        return result





    """*
    * Determines if this chart has a "y2" (right) y-axis.
    * <p>
    * Only charts that have at least one curve on the right
    * y axis will have a y2-axis.
    *
    * @return True if the chart has a second y axis, False otherwise.
    *
    * @see Curve#setYAxis Curve.setYAxis
    """
    def hasY2Axis(self):
        result = getY2Axis().getNCurvesVisibleOnAxis() > 0
        return result

    """*
    * Determines if this chart has an ordinary, or left, y-axis.
    * <p>
    * Only charts that have at least one curve on the left
    * y axis will have a y-axis.
    *
    * @return True if the chart has a left y axis, False otherwise
    *
    * @see Curve#setYAxis Curve.setYAxis
    *
    """
    def hasYAxis(self):
        result = getYAxis().getNCurvesVisibleOnAxis() > 0
        return result

    """*
    * Determines if the legend of this chart is visible.
    *
    *
    * @return True if the legend is visible, False otherwise.
    *
    * @see #setLegendVisible setLegendVisible
    """
    def isLegendVisible(self):
        return self.isLegendVisible



    """*
    *
    * Is the in-browser rendition of the chart inconsistent with
    * the current chart specs? In other words, is a call to
    * GChart's <tt>update</tt> method needed to bring the
    * browser's display into agreement with current chart specs?
    * <p>
    *
    * <i>Note:</i> Whenever this method returns
    * <tt>True</tt>, GChart "freezes" hover feedback, and
    * can no longer actively track the currently "touched"
    * point.  This is because GChart, to simplify its
    * bookkeeping, assumes in-browser (DOM) rendering and
    * current chart specs are in synch when determining the
    * point selection consequences of mouse events over the
    * chart.
    *
    * @return True if a call to <tt>update</tt> is needed to
    * bring current chart specifications and browser-rendered
    * representation into synch, False otherwise.
    *
    * @see #update update
    * @see #getTouchedPoint getTouchedPoint
    *
    """
    def isUpdateNeeded(self):
        result = self.chartDecorationsChanged  or not self.plotPanel.isValidated()
        return result


    """*
    * Removes the curve at the specified positional index.
    * <p>
    *
    * @param iCurve index of the curve to be removed
    *
    * @see #removeCurve(Curve) removeCurve(Curve)
    * @see #getCurve getCurve
    * @see #addCurve() addCurve()
    * @see #addCurve(int) addCurve(int)
    * @see #clearCurves clearCurves
    * @see #getNCurves getNCurves
    """
    def removeCurve(self, iCurve):
        if iCurve >= self.getNCurves():
            raise IllegalArgumentException(
            "iCurve = " + iCurve +"; iCurve may not exceed self.getNCurves()-1 (" + (self.getNCurves()-1) + ")")

        elif iCurve < 0:
            raise IllegalArgumentException(
            "iCurve = " + iCurve +"; iCurve may not be negative.")


        invalidateDependentSlices(iCurve)

        """
        * Simulate user moving away from point before it is deleted (this
        * assures that any required hoverCleanup gets called, and clears
        * the otherwise dangling reference to the touched point).
        *
        """
        if self.plotPanel.touchedPoint is not None  and  self.plotPanel.touchedPoint.getParent() == getSystemCurve(iCurve):

            self.plotPanel.touch(None)


        # remove the rendering panel that corresponds to this curve
        # (must keep the two lists in synch or 1-to-1 mapping breaks)
        internalIndex = internalCurveIndex(iCurve)
        if 0 != self.plotPanel.getRenderingPanelCount():
            rpIndex = getRenderingPanelIndex(internalIndex)
            self.plotPanel.removeGraphicsRenderingPanel(rpIndex)
            self.plotPanel.removeAnnotationRenderingPanel(rpIndex)


        c = self.curves.get(internalIndex)
        if c.isVisible():
            getXAxis().decrementCurves()
            if c.getYAxis() == Y_AXIS:
                getYAxis().decrementCurves()

            else:
                getY2Axis().decrementCurves()


        c.clearIndex()
        # else before 1st update, no rendering panels created yet
        self.curves.remove(internalIndex)
        # adjust ArrayList indexes to account for newly removed element
        for i in range(internalIndex, len(self.curves)):
            self.curves.get(i).decrementIndex()



    """*
    * Removes the given curve from this GChart.
    * <p>
    *
    * If the given curve is <tt>None</tt> or is not a curve on this GChart,
    * an exception is thrown.
    *
    * <p>
    *
    * @param curve the curve to be removed.
    *
    * @see #removeCurve(int) removeCurve(int)
    *
    """

    def removeCurve(self, curve):
        if None == curve:
            raise IllegalArgumentException("Curve cannot be None.")

        index = getCurveIndex(curve)
        if index == GChart.NAI:
            raise IllegalArgumentException("Curve is not one of this GChart's curves.")


        if index < 0:
            raise IllegalArgumentException("System curves cannot be removed (this should be impossible; a GChart bug is likely.)")

        else:
            removeCurve(index)



    """*
    ** Specifies the background color of the chart as a whole.
    **
    ** <p>
    ** The default background color is <tt>USE_CSS</tt>.
    ** <p>
    **
    ** For more information on standard CSS color
    ** specifications see the discussion in
    ** {@link Symbol#setBackgroundColor Symbol.setBackgroundColor}.
    ** <p>
    **
    ** @param cssColor the chart's background color, in a standard
    **   CSS color string format.
    **
    **
    ** @see #USE_CSS USE_CSS
    **
    *"""
    def setBackgroundColor(self, cssColor):
        self.chartDecorationsChanged = True
        self.backgroundColor = cssColor


    """*
    ** Specifies a URL that points to the transparent, 1 x 1 pixel,
    ** "blank GIF" that GChart uses in order to render your
    ** chart without adding spurious "missing image" icons to it.
    ** <p>
    **
    ** When GWT compiles an application that imports the GChart
    ** library, it automatically adds an appropriate blank
    ** image, <tt>gchart.gif</tt>, to the module base directory
    ** (this is the directory into which GWT also copies your
    ** compiled Javascript, all the files in your public
    ** directory, etc.).  <p>
    **
    ** By default, GChart uses the following blank image URL:
    ** <p>
    **
    ** <pre>
    **   GWT.getModuleBaseURL() + "gchart.gif"
    ** </pre>
    ** <p>
    **
    ** <small> Earlier versions used "gchart.gif" as this default url.
    ** <a href="http:#groups.google.com/group/Google-Web-Toolkit/msg/4be3f19dc14f958a">
    ** This GWT forum post by Dean S. Jones</a> identified the
    ** need to add the <tt>GWT.getModuleBaseURL()</tt> prefix.
    ** </small>
    ** <p>
    **
    ** Note that this default adds a potentially very
    ** long URL to every <tt>img</tt> element added by GChart to
    ** render your chart, which can (in theory) more than double
    ** the memory required to represent your chart in the
    ** browser, because the absolute URLs can be of undetermined
    ** length.  In practice, browser memory usage increases of
    ** 10% have been observed with the on-line demo GChart and a
    ** typicial, 60-odd character absolute URL.  <p>
    **
    ** You have several alternatives to the above default that can
    ** often reduce the length of the URL and thus save browser
    ** memory:
    **
    ** <p>
    **
    ** <ol> <li>Simply copy <tt>gchart.gif</tt> from the module
    **   base directory into your host page's base directory, and
    **   then use <tt>setBlankImageURL("gchart.gif")</tt> to access
    **   this URL relatively.
    **
    **   <li>If the relative path from the host page base
    **       directory to the module base directory is
    **       reasonably short, pass that alternative
    **       relative URL to this method (note that all
    **       relative URLs are interpreted relative to the base
    **       directory of the host page containing your GChart).
    **
    **   <li>Place a copy of <tt>gchart.gif</tt> into
    **       a directory whose absolute URL is very short,
    **       and then pass that short absolute URL to this method.
    **
    ** </ol>
    ** <p>
    **
    ** <small> <i>Special note to anyone reading
    ** this who designed HTML's <tt>image</tt> tag:</i> If you
    ** had provided a <tt>src=none</tt> option, this method
    ** would not have to exist.
    ** </small>
    ** <p>
    **
    ** <i>Tip:</i> If you already have an appropriate blank
    ** gif on your site that is accessible from the host
    ** page via a reasonably short URL there is no need to
    ** copy <tt>gchart.gif</tt>. You can just pass that URL
    ** to this method.
    **
    ** <p>
    **
    ** <i>Note:</i> Though GChart uses this blank image by default,
    ** you can use the <tt>setImageURL</tt> method to specify a
    ** non-blank image for use in rendering a specific curve.
    ** <p>
    **
    **
    ** @param blankImageURL a URL that points to a 1 x 1 pixel
    ** transparent image that GChart needs to render your
    ** charts without adding a spurious "missing image" icon.
    **
    ** @see #getBlankImageURL getBlankImageURL
    ** @see #DEFAULT_BLANK_IMAGE_URL DEFAULT_BLANK_IMAGE_URL
    ** @see Symbol#setImageURL setImageURL
    **
    *"""

    def setBlankImageURL(self, _blankImageURL):
        if _blankImageURL != self.blankImageURL:
            self.blankImageURL = _blankImageURL
            # Decided not to prefetch blank image URL because 1) pre-fetching
            # doesn't improve performance noticably in tested browsers,
            # 2) there are reports of possible memory leaks associated with
            # its use in the GWT issue tracker, and 3) users can
            # easily do the prefetch on their own if they want to, and that
            # is really the right place to do a prefetch anyway.
            #          Image.prefetch(GChart.getBlankImageURL())



    """*
    * Defines this GChart's hover parameter interpreter.
    * <p>
    *
    * Hovertext template strings can include <tt>${</tt>...
    * <tt>}</tt> bracketed
    * references to built-in parameters such as <tt>${x}</tt>
    * and <tt>${y}</tt> that get get replaced with appropriate
    * string representations of the x or y values of the
    * hovered-over point in displayed hovertext. You can add
    * new, custom, named parameters, and/or redefine the
    * meaning of built-in parameters, by passing a hover parameter
    * interpreter to this method.
    * <p>
    *
    * For sample code that shows you how to define a hover
    * parameter interpreter, see <tt>HoverParameterInterpreter</tt>.
    *
    * @see HoverParameterInterpreter HoverParameterInterpreter
    * @see Symbol#setHovertextTemplate setHovertextTemplate
    *
    * @param hpi the hover parameter interpreter to use with all
    * hovertext templates on this GChart (this interpreter is
    * responsible for replacing <tt>${</tt>...<tt>}</tt>
    * bracketed embedded parameter names in the hover text
    * template with appropriate HTML snippets representing the
    * value of that parameter at the hovered-over point).
    *
    """
    def setHoverParameterInterpreter(self, hpi):
        self.hoverParameterInterpreter = hpi


    """*
    * Specifies if merely hovering over a point is sufficient to select
    * it and display its hover annotation (<tt>True</tt>), or if an
    * actual click is needed (<tt>False</tt>).  <p>
    *
    * With the default of <tt>True</tt>, points are auto-selected as
    * the user "touches" them with the mouse-attached "brush"--no
    * clicking is required.  <p>
    *
    * When hover touching is disabled, a GChart can be used in a manner
    * analogous to a single-selection (sorry there's no multi-selection
    * capability) listbox, with its click-selectable points playing the
    * role of the selectable list items.  Specifically, disabling hover
    * touching lets you move the mouse freely without any danger of
    * changing the selected point--the point even remains selected if
    * the mouse moves entirely off the chart. This is helpful when your
    * application follows the common pattern of "select the thing you
    * want to operate on, then issue a command that operates on that
    * thing". This option is also helpful if you use very
    * compute-intensive hover widgets, or if you simply prefer
    * explictly-clicked-open/closed pop-up annotations.<p>
    *
    * <small> <i>How to Stop Leaky Clicks:</i> In IE7 and the hosted
    * mode browser, clicking ahead on a <tt>Button</tt> widget "leaks"
    * clicks upwards to the enclosing parent, even if you call
    * <tt>event.cancelBubble(True)</tt>. Such "leaky clicks" can
    * inappropriately change the selected point, when you really just
    * wanted to operate on it. This does not happen in Firefox 2, 3, or
    * Chrome, whose buttons properly "eat" the clicks--even when they
    * come in fast. To workaround the problem, you can place the
    * buttons into a hover widget (as shown in
    * <tt>GChartExample21.java</tt> in the chart gallery). This works
    * because GChart applies checks that ignore any mouse events that
    * occur within the rectangular region associated with the opened
    * hover widget.  </small> <p>
    *
    * For an example that uses <tt>setHoverTouchingEnabled(False)</tt>
    * to allow the user to change the y-value of the selected point,
    * see the Chart Gallery's <a
    * href="package-summary.html#GChartExample21"> GChartExample21</a>.
    *
    *
    * @param hoverTouchingEnabled <tt>True</tt> (the default) if you
    *   want users to be able to select points simply by hovering over
    *   them with their mouse, <tt>False</tt> if you want to
    *   require that they actually click on points to select them.
    *
    * @see #getHoverTouchingEnabled getHoverTouchingEnabled
    * @see Symbol#setBrushHeight setBrushHeight
    * @see #touch touch
    * @see #update update
    * @see HoverUpdateable HoverUpdateable
    *
    """
    def setHoverTouchingEnabled(self, hoverTouchingEnabled):
        self.hoverTouchingEnabled = hoverTouchingEnabled

    """*
    ** Specifies the color of the border around the chart as
    ** a whole.
    **
    ** <p>
    ** The default border color is <tt>USE_CSS</tt>.
    **
    ** <p>
    ** <blockquote><small>
    ** <i>Tip:</i> No border will appear if either <tt>borderStyle</tt>
    ** is <tt>none</tt>, <tt>borderWidth</tt> is <tt>0px</tt> or
    ** <tt>borderColor</tt> is <tt>transparent</tt>. Since
    ** these will often be the "CSS inherited" values,
    ** generally, it's best to set all three properties
    ** whenever you set any one of them.
    ** </small></blockquote>
    ** <p>
    **
    **
    ** For more information on standard CSS color
    ** specifications see the discussion in
    ** {@link Symbol#setBackgroundColor Symbol.setBackgroundColor}.
    ** <p>
    **
    ** @param cssColor the color of the chart's border, in a standard
    **   CSS color string format.
    **
    ** @see #setBorderWidth(String) setBorderWidth
    ** @see #setBorderStyle(String) setBorderStyle
    ** @see #getBorderColor getBorderColor
    ** @see #USE_CSS USE_CSS
    **
    *"""
    def setBorderColor(self, cssColor):
        self.chartDecorationsChanged = True
        if self.borderColor is None  or  self.borderColor == TRANSPARENT_BORDER_COLOR:
            raise IllegalArgumentException(
            "None and TRANSPARENT_BORDER_COLOR are not allowed. This method requires a valid CSS color specification String.")

        self.borderColor = cssColor


    """*
    ** Sets style of the border around the chart as a whole.
    **
    ** <p>
    ** The default border style is <tt>USE_CSS</tt>.
    ** <p>
    **
    ** <p>
    ** <blockquote><small>
    ** <i>Tip:</i> No border will appear if either <tt>borderStyle</tt>
    ** is <tt>none</tt>, <tt>borderWidth</tt> is <tt>0px</tt> or
    ** <tt>borderColor</tt> is <tt>transparent</tt>. Since
    ** these will often be the "CSS inherited" values,
    ** generally, it's best to set all three properties
    ** whenever you set any one of them.
    ** </small></blockquote>
    ** <p>
    **
    **
    ** @param borderStyle a CSS border style such as
    ** "solid", "dotted", "dashed", etc.
    **
    ** @see #getBorderStyle getBorderStyle
    ** @see #setBackgroundColor(String) setBackgroundColor
    ** @see #setBorderColor(String) setBorderColor
    ** @see #setBorderWidth(String) setBorderWidth
    ** @see #USE_CSS USE_CSS
    **
    **
    *"""
    def setBorderStyle(self, borderStyle):
        self.chartDecorationsChanged = True
        self.borderStyle = borderStyle


    """*
    ** Specifies the width of the border around the chart as a whole.
    **
    ** <p>
    ** The default border width is <tt>USE_CSS</tt>.
    **
    ** <p>
    ** <blockquote><small>
    ** <i>Tip:</i> No border will appear if either <tt>borderStyle</tt>
    ** is <tt>none</tt>, <tt>borderWidth</tt> is <tt>0px</tt> or
    ** <tt>borderColor</tt> is <tt>transparent</tt>. Since
    ** these will often be the "CSS inherited" values,
    ** generally, it's best to set all three properties
    ** whenever you set any one of them.
    ** </small></blockquote>
    **
    ** @param cssWidth width of the border around the chart as a whole,
    **   expressed as a CSS border-width specification string, such
    **   as "1px".
    **
    ** @see #getBorderWidth getBorderWidth
    ** @see #setBorderStyle(String) setBorderStyle
    ** @see #setBorderColor(String) setBorderColor
    ** @see #USE_CSS USE_CSS
    *"""
    def setBorderWidth(self, cssWidth):
        self.chartDecorationsChanged = True
        self.borderWidth = cssWidth



    """*
    * Convenience method equivalent to
    * <tt>setChartFootnotes(HTML(html))</tt>.
    *
    * @param html HTML text used to define the chart's title.
    *
    * @see #setChartFootnotes(Widget) setChartFootnotes(Widget)
    """
    def setChartFootnotes(self, html):
        setChartFootnotes(HTML(html))

    """* Sets widget that appears just below the chart.
    *  <p>
    *
    *  The widget will vertically centered within a band just
    *  below the x axis label that stretches along the entire
    *  bottom edge of the chart, and whose height is defined by
    *  <tt>setChartFootnotesThickness</tt>.
    *
    *  <p>
    *
    *  The widget will either be left justified, or horizontally
    *  centered, within this band depending on the property
    *  defined by <tt>setChartFootnotesLeftJustified</tt>
    *
    *
    *  @param chartFootnotes widget representing the chart's footnotes
    *
    *  @see #setChartFootnotes(String) setChartFootnotes(String)
    *  @see #setChartFootnotesThickness setChartFootnotesThickness
    *  @see #getChartFootnotes getChartFootnotes
    *  @see #setChartFootnotesLeftJustified
    *  setChartFootnotesLeftJustified
    """
    def setChartFootnotes(self, chartFootnotes):
        self.chartDecorationsChanged = True
        self.chartFootnotes = chartFootnotes


    """* Defines if this chart's footnotes are left justified,
    *  or horizontally centered across the bottom edge of the
    *  chart.
    *  <p>
    *  Note that a chart's footnotes are always vertically
    *  centered within the band at the bottom of the chart
    *  reserved for chart footnotes. Use the
    *  <tt>setChartFootnotesThickness</tt> method to set the
    *  height of this band.
    *
    *  @param footnotesLeftJustified True to position chart footnotes
    *  flush against the left edge of the chart, False (the default) to
    *  center them horizontally across the chart's bottom edge.
    *
    *  @see #setChartFootnotes(String) setChartFootnotes(String)
    *  @see #getChartFootnotes getChartFootnotes
    *  @see #setChartFootnotesThickness
    """
    def setChartFootnotesLeftJustified(self, footnotesLeftJustified):
        self.chartDecorationsChanged = True
        chartFootnotesLeftJustified = footnotesLeftJustified


    """*
    ** Sets the thickness (height) of the rectangular region at
    ** the bottom of the chart allocated for the footnotes.
    ** <p>
    **
    ** The width of this region always equals the width of
    ** the entire GChart (including legend and axis labels).
    ** <p>
    **
    ** Your footnotes widget is always vertically centered
    ** in this region.
    ** <p>
    **
    **
    ** Your footnotes widget will either be horizontally
    ** centered in this region, or left justified in it,
    ** depending on the property defined by the
    ** <tt>setChartFootnotesLeftJustified</tt> method.
    ** <p>
    **
    ** This setting has no impact on chart layout if the
    ** footnotes widget is <tt>None</tt> (the default); the
    ** rectangular footnotes region is entirely eliminated, and
    ** in effect has a 0 thickness, in that case.
    ** <p>
    **
    ** If you set the footnotes thickness to <tt>GChart.NAI</tt>
    ** (the default) GChart will use a thickness based on
    ** the estimated number of (<tt>&lt;br&gt;</tt> or
    ** <tt>&lt;li&gt;</tt>
    ** delimited) lines.
    **
    ** @param thickness the thickness (height) of the rectangle
    ** that contains the footnotes, in pixels, or
    ** <tt>GChart.NAI</tt> to use the default thickness.
    **
    ** @see #getChartFootnotesThickness getChartFootnotesThickness
    ** @see #setChartFootnotesLeftJustified setChartFootnotesLeftJustified
    ** @see GChart#NAI GChart.NAI
    ** @see #DEFAULT_FOOTNOTES_THICKNESS
    ** DEFAULT_FOOTNOTES_THICKNESS
    **
    *"""
    def setChartFootnotesThickness(self, thickness):
        self.chartDecorationsChanged = True
        self.footnotesThickness = thickness


    """*
    * Convenience method equivalent to
    * <tt>setXChartSize(xChartSize); setYChartSize(yChartSize)</tt>.
    *
    * @param xChartSize number of x-pixels in the curve
    *   display area of the chart
    * @param yChartSize number of y-pixels in the curve
    *   display area of the chart
    *
    * @see #setXChartSize setXChartSize
    * @see #setYChartSize setYChartSize
    *
    """
    def setChartSize(self, xChartSize, yChartSize):
        setXChartSize(xChartSize)
        setYChartSize(yChartSize)


    """*
    * Convenience method equivalent to
    * <tt>setChartTitle(HTML(html))</tt>.
    *
    * @param html HTML text used to define the chart's title.
    *
    * @see #setChartTitle(Widget) setChartTitle(Widget)
    """
    def setChartTitle(self, html):
        setChartTitle(HTML(html))


    # returns x,y min/max over every plotted curve

    """*
    * Specifies the widget that appears centered just above the chart.
    *
    * @param chartTitle the widget to be used as this chart's title.
    *
    * @see #setChartTitle(String) setChartTitle(String)
    * @see #setChartTitleThickness setChartTitleThickness
    * @see #getChartTitle getChartTitle
    *
    """
    def setChartTitle(self, chartTitle):
        self.chartDecorationsChanged = True
        self.chartTitle = chartTitle


    """*
    ** Sets the thickness (height) of the rectangular region at
    ** the top of the chart allocated for the title.
    ** <p>
    **
    ** Your title widget is always centered vertically and
    ** horizontally within this rectangular region. <p>
    **
    ** This setting has no impact on chart layout if the title
    ** widget is <tt>None</tt>, since the title-holding
    ** region is entirely eliminated in that case.
    **
    ** If you set the title thickness to <tt>GChart.NAI</tt>
    ** (the default) GChart will use a thickness that is
    ** based on the the number of <tt>&lt;br&gt;</tt> or
    ** <tt>&lt;li&gt;</tt> delimited HTML lines if the title Widget
    ** implements <tt>HasHTML</tt>.
    **
    ** @param thickness the thickness (height) of the rectangle
    ** that contains the title, in pixels, or
    ** <tt>GChart.NAI</tt> to use the default thickness.
    **
    ** @see #getChartTitleThickness getChartTitleThickness
    ** @see GChart#NAI GChart.NAI
    ** @see #DEFAULT_TITLE_THICKNESS
    ** DEFAULT_TITLE_THICKNESS
    **
    *"""
    def setChartTitleThickness(self, thickness):
        self.chartDecorationsChanged = True
        self.titleThickness = thickness


    """*
    * Specifies if this chart will clip any rendered chart elements
    * (including hover selection feedback and popup annotations)
    * that extends beyond the bounds of the decorated chart.
    * <p>
    *
    * The decorated chart includes not just the plot area, but
    * space allocated for titles, footnotes, legend key, axis
    * labels, tick marks, etc. The size of this decorated chart
    * can be obtained via the <tt>getXChartSizeDecorated</tt>
    * and <tt>getYChartSizeDecorated</tt> methods.
    * <p>
    *
    * <small> Note that, in non-IE browsers, drawing a curve via
    * <tt>GWTCanvas</tt> that falls outside the bounds of the
    * decorated chart could occlude mouse events over elements
    * on the enclosing page <i>that fall within the smallest
    * bounding rectangle that contains the canvas-rendered
    * curve</i>. HTML rendering (IE's element-based VML used by
    * <tt>GWTCanvas</tt> is essentially HTML-like in this respect) only
    * creates such occlusions at the positions where the curve
    * is actually rendered.  </small>
    *
    * @param clipToDecoratedChart use <tt>True</tt> to clip
    * off-the-decorated-chart symbols, annotations, etc.  or
    * <tt>False</tt> (the default) to allow such chart elements to be
    * drawn outside of the rectangular region allocated for the
    * chart.
    *
    * @see #getClipToDecoratedChart getClipToDecoratedChart
    * @see #setClipToPlotArea setClipToPlotArea
    * @see #getXChartSizeDecorated getXChartSizeDecorated
    * @see #getYChartSizeDecorated getYChartSizeDecorated
    * @see #setCanvasFactory setCanvasFactory
    *
    """

    def setClipToDecoratedChart(self, clipToDecoratedChart):
        self.chartDecorationsChanged = True
        invalidateAccessibleCurves()
        self.clipToDecoratedChart = clipToDecoratedChart

    """* Specifies if rendered graphics falling
    ** outside the plot area will be clipped off.
    *  <p>
    *
    *  <i>Note:</i> This clipping does not apply to the hover selection
    *  feedback. In particular, points that fall outside the plot area,
    *  though not visible, will still display their selection feedback
    *  and pop-up hover annotations when the user mouses over them.
    *
    * @param clipToPlotArea <tt>False</tt> (the default) to display
    *   off-the-plot-area graphics,
    *   <tt>True</tt>
    *   to clip them off.
    *
    * @see #getClipToPlotArea getClipToPlotArea
    * @see #setClipToDecoratedChart setClipToDecoratedChart
    *
    """
    def setClipToPlotArea(self, clipToPlotArea):
        self.chartDecorationsChanged = True
        invalidateAccessibleCurves()
        self.clipToPlotArea = clipToPlotArea

    """*
    * Sets the symbol border colors that are used by default for
    * newly created curves. The
    * array must contain one or more elements, each a standard
    * CSS or RGBA color specification string (see the
    * <tt>setBackgroundColor</tt> link below for more
    * on CSS color specification strings) or the
    * special GChart keyword <tt>TRANSPARENT_BORDER_COLOR</tt>.
    * <p>
    *
    * GChart uses the first color in this array as the default border
    * color of the first curve added (via <tt>addCurve</tt>), the
    * second color for the second curve added, and so on. If more
    * curves are added than the number of elements in the default
    * border colors array, the sequence is repeated.
    *
    * <p>
    * <small>
    * Note that each curve/symbol's default color is "locked in" at the
    * point when that curve/symbol is first added, based on the
    * total number of curves at that time.
    * </small>
    *
    * <p>
    *
    * Because, by default, GChart uses a transparent symbol background
    * color, the default border color will usually, in effect, define
    * the default color of each curve. The default border color
    * also defines the
    * default color of point-to-point connecting lines in a line
    * chart.<p>
    *
    * If not explicitly specified via this method, GChart uses
    * <tt>GChart.DEFAULT_SYMBOL_BORDER_COLORS</tt> by default.
    * However, most people find the
    * color sequence <a href=
    * "http:#ui.openoffice.org/VisualDesign/OOoChart_colors_drafts.html#02">
    * used by OpenOffice's Charts</a> more aesthetically pleasing.
    * The <a
    * href="package-summary.html#GChartExample22a">World's Simplest
    * Line Chart Editor</a> example chart contains a line of
    * code that makes GChart use the OpenOffice defaults.
    * <p>
    *
    * <small>This feature was added in response to an email from
    * <a href="http:#www.profilercorp.com">Joe Cole</a>
    * and <a href="http:#gwt-ext.com/forum/viewtopic.php?f=13&t=3465&start=3">
    this post</a> by Sanjiv Jivan.
    * They both pointed out the importance of changing GChart's
    * default colors.</small>
    *
    *
    * @param defaultBorderColors array of CSS color strings
    * whose successive elements define the initial symbol border colors
    * for curves in the order that they are added.
    *
    * @see #DEFAULT_SYMBOL_BORDER_COLORS DEFAULT_SYMBOL_BORDER_COLORS
    * @see #TRANSPARENT_BORDER_COLOR TRANSPARENT_BORDER_COLOR
    * @see Symbol#setBackgroundColor setBackgroundColor
    * @see Symbol#setBorderColor setBorderColor
    * @see #addCurve addCurve
    *
    """

    def setDefaultSymbolBorderColors(self, defaultBorderColors):
        if None == defaultBorderColors:
            raise IllegalArgumentException(
            "defaultBorderColors array cannot be None.")

        elif defaultBorderColors.length < 1:
            raise IllegalArgumentException(
            "defaultBorderColors array must have at least 1 element.")

        else:
            self.defaultSymbolBorderColors = defaultBorderColors




    """* Sets the font-family used in tick labels, point annotations,
    ** legends, titles, footnotes, and
    ** axis labels.
    ** <p>
    ** If not specified, the default value is <tt>USE_CSS</tt>.
    ** <p>
    **
    ** Note that titles, footnotes and axis labels are
    ** defined via externally created Widgets, which are free
    ** to override the font-family specified by this
    ** method.
    **
    ** @param fontFamily a CSS font-family specification, such
    **   as "Arial, sans-serif"
    **
    ** @see #getFontFamily getFontFamily
    ** @see #USE_CSS USE_CSS
    **
    *"""
    def setFontFamily(self, fontFamily):
        self.chartDecorationsChanged = True
        self.fontFamily = fontFamily




    """*
    ** Specifies the single color used for all gridlines, axes
    ** lines, and tick marks.
    **
    **
    ** <p>
    ** For more information on standard CSS color
    ** specifications see the discussion in
    ** {@link Symbol#setBackgroundColor Symbol.setBackgroundColor}.
    ** <p>
    **
    ** @param cssColor the color, in CSS standard color format,
    **    to be used for all gridlines, axes, and tick marks.
    **
    ** @see #getGridColor getGridColor
    ** @see #DEFAULT_GRID_COLOR DEFAULT_GRID_COLOR
    **
    *"""
    def setGridColor(self, cssColor):
        #TODO: support line style for dotted/dashed gridlines lines,
        # allow tick and grid colors to be specified separately, etc.
        getSystemCurve(XGRIDLINES_ID).getSymbol().setBorderColor(cssColor)
        getSystemCurve(YGRIDLINES_ID).getSymbol().setBorderColor(cssColor)
        getSystemCurve(Y2GRIDLINES_ID).getSymbol().setBorderColor(cssColor)
        getSystemCurve(XAXIS_ID).getSymbol().setBorderColor(cssColor)
        getSystemCurve(YAXIS_ID).getSymbol().setBorderColor(cssColor)
        getSystemCurve(Y2AXIS_ID).getSymbol().setBorderColor(cssColor)
        getSystemCurve(XTICKS_ID).getSymbol().setBorderColor(cssColor)
        getSystemCurve(YTICKS_ID).getSymbol().setBorderColor(cssColor)
        getSystemCurve(Y2TICKS_ID).getSymbol().setBorderColor(cssColor)

    """*
    ** Sets the background color of the chart's legend.
    **
    **
    ** <p>
    ** For more information on standard CSS color
    ** specifications see the discussion in
    ** {@link Symbol#setBackgroundColor Symbol.setBackgroundColor}.
    ** <p>
    **
    ** @param cssColor the legend's background color, in a standard
    **   CSS color string format.
    **
    ** @see #getLegendBackgroundColor getLegendBackgroundColor
    ** @see #DEFAULT_LEGEND_BACKGROUND_COLOR
    **       DEFAULT_LEGEND_BACKGROUND_COLOR
    *"""
    def setLegendBackgroundColor(self, cssColor):
        self.chartDecorationsChanged = True
        self.legendBackgroundColor = cssColor

    """*
    ** Sets the border color of the chart's legend.
    **
    **
    ** <p>
    ** For more information on standard CSS color
    ** specifications see the discussion in
    ** {@link Symbol#setBackgroundColor Symbol.setBackgroundColor}.
    ** <p>
    **
    ** @param cssColor the color of the legend's border, in a standard
    **   CSS color string format, of the special GChart keyword
    **   <tt>TRANSPARENT_BORDER_COLOR</tt> for a transparent border.
    **
    **
    ** @see #getLegendBorderColor getLegendBorderColor
    ** @see #DEFAULT_LEGEND_BORDER_COLOR DEFAULT_LEGEND_BORDER_COLOR
    ** @see #TRANSPARENT_BORDER_COLOR TRANSPARENT_BORDER_COLOR
    **
    *"""
    def setLegendBorderColor(self, cssColor):
        self.chartDecorationsChanged = True
        self.legendBorderColor = cssColor

    """*
    ** Sets the width of the chart legend's border.
    **
    ** @param width the width of the legend's border, in pixels
    **
    ** @see #getLegendBorderWidth getLegendBorderWidth
    ** @see #DEFAULT_LEGEND_BORDER_WIDTH DEFAULT_LEGEND_BORDER_WIDTH
    *"""
    def setLegendBorderWidth(self, width):
        self.chartDecorationsChanged = True
        self.legendBorderWidth = width

    """*
    ** Sets style of the border around the chart's legend (key).
    **
    ** <p>
    **
    ** <p>
    ** @param borderStyle a CSS border style such as
    ** "solid", "dotted", "dashed", etc.
    **
    ** @see #getLegendBorderStyle getLegendBorderStyle
    ** @see #setLegendBackgroundColor setLegendBackgroundColor
    ** @see #setLegendBorderColor setLegendBorderColor
    ** @see #DEFAULT_LEGEND_BORDER_STYLE DEFAULT_LEGEND_BORDER_STYLE
    *"""
    def setLegendBorderStyle(self, borderStyle):
        self.chartDecorationsChanged = True
        self.legendBorderStyle = borderStyle

    """*
    ** Specifies the color of the legend's font. Default is
    ** <tt>DEFAULT_FONT_COLOR</tt>.
    **
    **
    ** <p>
    ** For more information on standard CSS color
    ** specifications see the discussion in
    ** {@link Symbol#setBackgroundColor Symbol.setBackgroundColor}.
    ** <p>
    **
    ** @param cssColor color of the font used to display the
    **    labels in the legend.
    **
    ** @see #getLegendFontColor getLegendFontColor
    ** @see #DEFAULT_FONT_COLOR DEFAULT_FONT_COLOR
    **
    *"""
    def setLegendFontColor(self, cssColor):
        self.chartDecorationsChanged = True
        self.legendFontColor = cssColor


    """*
    * Specifies the CSS font size, in pixels, of text displayed
    * in the chart's legend (also know as a chart's key).
    * <p>
    * This size also governs the size of the symbol icon
    * displayed in the legend.
    * <p>
    * Default is <tt>DEFAULT_LEGEND_FONTSIZE</tt>.
    *
    * @param legendFontSize the font size of legend text
    *
    * @see #getLegendFontSize getLegendFontSize
    * @see #DEFAULT_LEGEND_FONTSIZE DEFAULT_LEGEND_FONTSIZE
    *
    """
    def setLegendFontSize(self, legendFontSize):
        self.chartDecorationsChanged = True
        self.legendFontSize = legendFontSize

    """*
    ** Specifies the cssStyle of the font used to render the
    ** legend's labels. Default is <tt>DEFAULT_FONT_STYLE</tt>.
    **
    ** @param cssStyle any valid CSS font-style, namely,
    **   normal, italic, oblique, or inherit.
    **
    ** @see #getLegendFontStyle getLegendFontStyle
    ** @see #DEFAULT_FONT_STYLE DEFAULT_FONT_STYLE
    *"""
    def setLegendFontStyle(self, cssStyle):
        self.chartDecorationsChanged = True
        self.legendFontStyle = cssStyle


    """*
    ** Specifies the weight of the font used in the labels of the
    ** legend. Default is <tt>DEFAULT_FONT_WEIGHT</tt>.
    **
    ** @param cssWeight a CSS font-weight specification, such as
    **    bold, bolder, normal, light, 100, 200, ... or 900.
    **
    ** @see #getLegendFontWeight getLegendFontWeight
    ** @see #DEFAULT_FONT_WEIGHT DEFAULT_FONT_WEIGHT
    *"""
    def setLegendFontWeight(self, cssWeight):
        self.chartDecorationsChanged = True
        self.legendFontWeight = cssWeight

    """*
    ** Sets the thickness (width) of the rectangular region at
    ** the right of the chart allocated for the legend key.
    ** <p>
    **
    ** This setting has no impact on chart layout if the
    ** legend key is not visible, since the legend key's
    ** rectangular region is entirely eliminated in that
    ** case.
    **
    ** <p>
    **
    ** If the legend thickness is set to <tt>GChart.NAI</tt>
    ** (the default) GChart uses an heuristic to set the legend
    ** thickness based on the number of characters in each
    ** curve's legend label.
    **
    **
    ** @param legendThickness the thickness (width) of the rectangle
    ** that contains the legend key, in pixels, or
    ** <tt>GChart.NAI</tt> to use a built-in heurstic
    ** to determine the legend width.
    **
    ** @see #getLegendThickness getLegendThickness
    ** @see Curve#setLegendLabel setLegendLabel
    ** @see Y2Axis#setAxisLabelThickness Y2Axis.setAxisLabelThickness
    **
    *"""
    def setLegendThickness(self, legendThickness):
        self.chartDecorationsChanged = True
        self.legendThickness = legendThickness


    """*
    * Specifies if the legend is to be visible on this chart.
    * Legends are visible by default. However, a legend is only
    * generated if at least one curve's legend label has been
    * specified.
    *
    * @param isLegendVisible True to display the legend, False to
    * hide it.
    *
    * @see #isLegendVisible isLegendVisible
    * @see Curve#setLegendLabel setLegendLabel
    """
    def setLegendVisible(self, isLegendVisible):
        self.chartDecorationsChanged = True
        self.isLegendVisible = isLegendVisible


    """*
    * By default, this property is <tt>False</tt>, which means
    * that GChart will retain no-longer-needed Image and Grid
    * widgets (plus any user object references associated with
    * those widgets, such as those created via the
    * <tt>setAnnotationText</tt> and
    * <tt>setAnnotationWidget</tt> methods) between
    * <tt>updates</tt> in the expectation that they may be
    * needed by future updates.  This strategy often makes
    * updates faster, because building Image and Grid
    * elements "from scratch" is very expensive.  However,
    * strictly speaking, GChart is holding onto memory it no
    * longer needs to render the chart <i>right now</i>--which
    * would normally be considered a memory leak if it were not
    * being done deliberately.  <p>
    *
    * If <tt>optimizeForMemory</tt> is set to <tt>True</tt>,
    * GChart will (at the very next <tt>update()</tt> call) free
    * up any Image or Grid elements that are no longer required
    * to render the current chart.  Should a chart's size grow back
    * to a former size, the subsequent update would be slower,
    * though.
    *
    * <p> Charts that use exactly the same number of Image and
    * Grid elements for each update (for example a bar chart
    * where the number of bars is fixed) will see no impact on
    * either memory use or update speeds by setting this
    * parameter.  Charts that have a highly variable number of
    * Image or Grid elements (for example, a chart whose number
    * of points varies randomly between 5 and 500) may see a
    * very large impact on speed (False is faster) or memory
    * (True is more compact).
    * <p>
    *
    * The setting of this parameter never has any impact on the
    * speed or memory used on the <i>very first</i> chart
    * update.
    * <p>
    *
    * In one test using the future oil price simulation chart of
    * GChart's live demo (which has only small changes in the
    * number of elements required to render the chart between
    * updates) setting this parameter to True made the updates,
    * on average, around 10% slower, but also reduced the memory
    * footprint by around 2%.
    *
    * @param optimizeForMemory <tt>True</tt> to optimize updates
    * to use less memory, <tt>False</tt> (the default) to
    * optimize them to use less time.
    *
    * @see #update update
    *
    """
    def setOptimizeForMemory(self, optimizeForMemory):
        self.optimizeForMemory = optimizeForMemory

    """*
    ** Specifies the amount of padding to add just inside of the
    ** chart's border, as a CSS padding specification string.
    ** <p>
    **
    ** <p>
    ** The default padding is <tt>USE_CSS</tt>.
    **
    ** <p>
    **
    ** @param cssPadding the width of the padding, as a CSS padding
    **   specification string
    **   (e.g. use "1px" to introduce a 1 pixel padding
    **   just between the chart' border and the chart itself)
    **
    ** @see #getPadding getPadding
    ** @see #setBorderWidth setBorderWidth
    ** @see #setBorderStyle(String) setBorderStyle
    ** @see #setBorderColor(String) setBorderColor
    ** @see #USE_CSS USE_CSS
    *"""
    def setPadding(self, cssPadding):
        self.chartDecorationsChanged = True
        self.padding = cssPadding


    """*
    ** Specifies the background color of the area of the chart
    ** in which symbols representing curve data are displayed
    **
    **
    ** <p>
    ** For more information on standard CSS color
    ** specifications see the discussion in
    ** {@link Symbol#setBackgroundColor Symbol.setBackgroundColor}.
    ** <p>
    **
    ** @param cssColor CSS color string defining the plot
    **    area's background color
    **
    ** @see #getPlotAreaBackgroundColor getPlotAreaBackgroundColor
    *"""
    def setPlotAreaBackgroundColor(self, cssColor):
        c = getSystemCurve(PLOTAREA_ID)
        c.getSymbol().setBackgroundColor(cssColor)


    """*
    ** Specifies the color of the border around the area of the
    ** chart in which symbols representing curve data are
    ** displayed.
    **
    **
    ** <p>
    ** For more information on standard CSS color
    ** specifications see the discussion in
    ** {@link Symbol#setBackgroundColor Symbol.setBackgroundColor}.
    ** <p>
    **
    ** @param cssColor CSS color string defining the color of
    **    the plot area's border
    **
    ** @see #getPlotAreaBorderColor getPlotAreaBorderColor
    *"""
    def setPlotAreaBorderColor(self, cssColor):
        c = getSystemCurve(PLOTAREA_ID)
        c.getSymbol().setBorderColor(cssColor)

    """*
    ** Specifies the width of the border around the area of the
    ** chart in which symbols representing curve data are
    ** displayed.
    **
    ** @param width the width, in pixels, of the border around
    **   the plot area
    **
    ** @see #getPlotAreaBorderWidth getPlotAreaBorderWidth
    *"""
    def setPlotAreaBorderWidth(self, width):
        c = getSystemCurve(PLOTAREA_ID)
        c.getSymbol().setBorderWidth(width)

    """*
    ** Sets style of the border around the chart's plot area
    ** (the rectangular area where the curves are drawn).
    **
    ** <p>
    **
    ** <p>
    ** @param borderStyle a CSS border style such as
    ** "solid", "dotted", "dashed", etc.
    **
    ** @see #getPlotAreaBorderStyle getPlotAreaBorderStyle
    ** @see #setPlotAreaBackgroundColor setPlotAreaBackgroundColor
    ** @see #setPlotAreaBorderColor setPlotAreaBorderColor
    *"""
    def setPlotAreaBorderStyle(self, borderStyle):
        c = getSystemCurve(PLOTAREA_ID)
        c.getSymbol().setBorderStyle(borderStyle)


    """*
    * Sets the image URL that defines the background of
    * the GChart plot area. The GChart plot area is the
    * rectangular region defined by the x and y axes of
    * the plot, but does not include those axes (or
    * their ticks).
    * <p>
    * Note that by default, or if this URL is set to <tt>None</tt>,
    * GChart will use the URL returned by
    * <tt>getBlankImageURL</tt>.
    * <p>
    *
    * <small><b>Ideas/tips for using the plot area background
    * URL:</b>
    * <blockquote>
    * <ol>
    *  <li> It's often best to
    *  exactly match the width and height of the image
    *  with the GChart plot area width and height
    *  (defined via (via <tt>setChartSize</tt>). Otherwise,
    *  the image will be scaled up or down to fit the
    *  plot area, which usually doesn't look that great.
    *
    *  <li>Note that since a Google Chart API url is just
    *  an image url to GChart, you can easily use a
    *  Google Chart API url to define the background of an
    *  otherwise client-side chart. For example, you
    *  might place a 3-D pie chart behind
    *  a rapidly changing client-side GChart bar chart.
    *
    * <li> Note that this method's image will appear <i>behind</i>
    * every gridline and curve on the chart.  To overlay
    * images <i>on top of</i> the gridlines or other curves, or
    * even to place them outside of the plot area, use a
    * dedicated curve and its symbol's <tt>setImageURL</tt>
    * method, or simply embed such images within HTML-defined
    * point annotations.
    * </ol>
    *
    * </blockquote></small>
    *
    * @see #getPlotAreaImageURL getPlotAreaImageURL
    * @see #setBlankImageURL setBlankImageURL
    * @see GChart.Symbol#setImageURL setImageURL
    *
    * @param imageURL URL of the image used as the background
    * of the plot area.
    *
    """

    def setPlotAreaImageURL(self, imageURL):
        c = getSystemCurve(PLOTAREA_ID)
        c.getSymbol().setImageURL(imageURL)


    """* @deprecated
    **
    ** Equivalent to
    ** <tt>setClipToPlotArea(!showOffChartPoints)</tt>.
    ** Use that method instead.
    ** <p>
    **
    ** <small>
    ** As of GChart 2.5, the clip-to-plot-area algorithm no
    ** longer drops the entire symbol if it's x,y coordinates
    ** are outside of the plot area; instead, it clips them
    ** off in the traditional "<tt>overflow: hidden</tt>" manner.
    ** Though unlikely you would need to, there is no easy way
    ** to recreate the previous behavior. <p>
    **
    ** This change was made so that both rectangular HTML and
    ** continuous, canvas-rendered
    ** chart elements would be clipped in a consistent and
    ** sensible way.
    ** </small>
    **
    ** @see #setClipToPlotArea setClipToPlotArea
    **
    *"""
    def setShowOffChartPoints(self, showOffChartPoints):
        self.setClipToPlotArea(not showOffChartPoints)



    """* @deprecated
    **
    ** Equivalent to
    ** setClipToDecoratedChart(!showOffDecoratedChart), please
    ** use that method instead.
    **
    ** @see #setClipToDecoratedChart setClipToDecoratedChart
    *"""
    def setShowOffDecoratedChartGlyphs(self, showOffDecoratedChartGlyphs):
        self.setClipToDecoratedChart(not showOffDecoratedChartGlyphs)


    """*
    * Returns the curve that the mouse "brush" is currently
    * "touching" (the so-called "hovered over" point), or <tt>None</tt>
    * if none.
    * <p>
    *
    * Convenience method equivalent to (when the touched point is
    * not <tt>None</tt>) <tt>getTouchedPoint().getParent()</tt>.
    * See <tt>getTouchedPoint</tt> for full details.
    * <p>
    *
    *
    * See the <tt>setBrushHeight</tt> method for the rules
    * GChart uses to determine the currently touched point.
    * <p>
    *
    *
    * @return a reference to the curve that the mouse "brush"
    * is currently "touching".
    *
    * @see #getTouchedPoint getTouchedPoint
    * @see Symbol#setBrushHeight setBrushHeight
    * @see Symbol#setHoverSelectionSymbolType
    *      setHoverSelectionSymbolType
    *
    """
    def getTouchedCurve(self):
        result = None
        if None != getTouchedPoint():
            result = getTouchedPoint().getParent()

        return result


    """*
    * Returns the point that the mouse "brush" is currently
    * "touching" (the so-called "hovered over" point), or <tt>None</tt>
    * if none.
    *
    * <p>
    *  <small> <i>Fine-print:</i> If the chart clicked on needs an
    *  update, this method returns the touched point <i>as
    *  of the last time the chart's in-browser (DOM) display was
    *  up-to-date</i>. If you don't assure that your chart's DOM display
    *  is up-to-date via other means (e.g. updating right after you
    *  change its specifications) a quick check with the
    *  <tt>isUpdateNeeded</tt> method and a subsequent <tt>update</tt>
    *  before accessing the touched point can be a good strategy.
    *  <p> </small>
    *
    *
    * See the <tt>setBrushHeight</tt> method for the rules
    * GChart uses to determine the currently touched point.
    * <p>
    *
    * <small>
    * <i>Warning:</i> The currently touched point, on FF2 (but not in
    * IE7) can be changed (or set to <tt>None</tt>) by invoking
    * <tt>Window.alert</tt>. Though I originally expected that such
    * a modal alert box would "eat" all mouse events (and it does
    * just that in IE7) in FF2 (and possibly other browsers)
    * some mouse events on the alert box are also passed on up to
    * the GChart. It's best for applications that need to "lock on"
    * to the <i>initially</i> touched point to grab a
    * reference to the touched point <i>before</i> performing any
    * activity that allows the user to interact with the
    * browser in ways that could possibly generate GChart-visible
    * mouse events.
    * </small>
    * <p>
    *
    * @return a reference to the point that the mouse "brush"
    * is currently "touching".
    *
    * @see #getTouchedCurve getTouchedCurve
    * @see #touch touch
    * @see Symbol#setBrushHeight setBrushHeight
    * @see Symbol#setHoverSelectionSymbolType
    *      setHoverSelectionSymbolType
    * @see #isUpdateNeeded isUpdateNeeded
    * @see #update update
    * @see Axis#getMouseCoordinate getMouseCoordinate
    * @see Axis#clientToModel clientToModel
    * @see Axis#modelToClient modelToClient
    * @see Axis#pixelToModel pixelToModel
    * @see Axis#modelToPixel modelToPixel
    *
    """
    def getTouchedPoint(self):
        return self.plotPanel.touchedPoint



    """*
    * Sets the number of pixels, in the horizontal
    * dimension, available for curve display. Note that
    * this curve display area does <i>not</i> include the
    * axes themselves, their tick marks, their labels, etc.
    *
    * <p>
    *
    * <i>Note</i>: Most modern display devices use "square"
    * pixels, that is, pixels whose width and height are
    * the same. GChart tacitly assumes square pixels in
    * many of its default settings.
    *
    *
    * @param xChartSize the number of x-pixels in the chart region
    *   used for curve display.
    *
    * @see #getXChartSize getXChartSize
    * @see #getXChartSizeDecorated getXChartSizeDecorated
    * @see #setYChartSize setYChartSize
    *
    """
    def setXChartSize(self, xChartSize):
        self.chartDecorationsChanged = True
        self.xChartSize = xChartSize
        c = getSystemCurve(PLOTAREA_ID)
        c.getSymbol().setWidth(xChartSize)


    """*
    * Sets the number of pixels, in the vertical dimension,
    * available for curve display. Note that this curve
    * display region of the chart does <i>not</i> include
    * the axes themselves, their tick marks, labels, etc.
    *
    * <p>
    *
    * <i>Note</i>: Most modern display devices use "square"
    * pixels, that is, pixels whose width and height are
    * the same. GChart tacitly assumes square pixels in
    * many of its default settings.
    *
    * @param yChartSize the number of y-pixels in the chart region
    *   used for curve display.
    *
    * @see #getYChartSize getYChartSize
    * @see #getYChartSizeDecorated getYChartSizeDecorated
    * @see #setXChartSize setXChartSize
    *
    """
    def setYChartSize(self, yChartSize):
        self.chartDecorationsChanged = True
        self.yChartSize = yChartSize
        c = getSystemCurve(PLOTAREA_ID)
        c.getSymbol().setHeight(yChartSize)


    """*
    * Simulates the user "touching" a point with the mouse, by
    * performing those operations that occur when the user "hovers
    * over" the specified point. In detail, this method does the
    * following:<p>
    *
    * <ol>
    *
    *  <li> The specified point is made the currently "touched point"
    *  (this is the reference returned by <tt>getTouchedPoint</tt>). <p>
    *
    *  <li>If the previously touched point had a hover widget,
    *  that hover widget's <tt>hoverCleanup</tt> method is called.<p>
    *
    *  <li>If the touched point has an associated hover widget, that
    *  widget's <tt>hoverUpdate</tt> method is called.<p>
    *
    *  <li> Any hover selection feedback or hover annotation on
    *  any previously touched point is removed.<p>
    *
    *  <li>Any hover annotation for the newly touched point is
    *  displayed as per the various hover annotation related
    *  specifications (e.g.  <tt>setHoverLocation</tt>) associated with
    *  the symbol used to render the point.<p>
    *
    *  <li> Any selection feedback for the newly touched point is
    *  displayed in accord with the hover selection feedback
    *  specificiations (e.g.  <tt>setHoverSelectionBorderColor</tt>)
    *  associated with the symbol used to render the point.<p>
    *
    *  </ol>
    *
    * Using <tt>None</tt> as the point to touch simulates
    * the user moving the mouse into a region where it is not
    * touching any point (for example, off the chart entirely).
    * <p>
    *
    * Note that, as with all chart specification changes, you must
    * invoke <tt>update</tt> before the point selection and other
    * changes associated with this method will appear on the chart.
    * <p>
    *
    * <i>Tip:</i> The touched point can sometimes be used in lieu of a
    * point selection capability (which GChart lacks). For example, a
    * dialog box that allowed users to choose data points by their
    * names could "touch" the point associated with a user-selected
    * name in order to highlight it on the chart.
    *
    * @param pointToTouch this method will perform appropriate
    *   operations (as described above) in order to simulate the user
    *   "touching" this point with their mouse.
    *
    * @see #getTouchedPoint getTouchedPoint
    * @see #getTouchedCurve getTouchedCurve
    * @see HoverUpdateable#hoverUpdate hoverUpdate
    * @see HoverUpdateable#hoverCleanup hoverCleanup
    * @see Symbol#setHoverWidget setHoverWidget
    * @see Symbol#setHoverLocation setHoverLocation
    * @see Symbol#setHoverSelectionBorderColor
    * setHoverSelectionBorderColor
    * @see Axis#getMouseCoordinate getMouseCoordinate
    * @see Axis#clientToModel clientToModel
    * @see Axis#modelToClient modelToClient
    * @see Axis#pixelToModel pixelToModel
    * @see Axis#modelToPixel modelToPixel
    *
    """
    def touch(self, pointToTouch):
        self.plotPanel.touch(pointToTouch)

    """*
    ** Builds a chart that reflects current user-specified
    ** chart specs (curve data, symbol choices, etc.)
    ** <p>
    **
    ** Before any of the chart specifications of the other
    ** methods of this class will actually be visible
    ** on the chart, you must call this method.
    ** <p>
    **
    ** Typically, for efficiency, you would call this
    ** method only after you had made all of the desired
    ** chart specifications via the other methods.
    **
    ** <p>
    **
    ** By default, updates are optimized for speed, and this
    ** can end up wasting (usually not too much, though there
    ** are exceptions) memory.  To optimize for memory
    ** instead, use the <tt>setOptimizeForMemory</tt> method.
    ** <p>
    **
    ** For a discussion of Client-side GChart update times and
    ** how minimize them, see
    ** <a
    ** href="{@docRoot}/com/googlecode/gchart/client/doc-files/tipsformakingupdatesfaster.html">
    ** Tips for Making Client-side GChart Updates Faster</a>.
    ** <p>
    **
    ** <i>Note</i> Hover feedback is disabled whenever the currently
    ** rendered chart does not match current chart specs, that is,
    ** whenever <tt>isUpdateNeeded</tt> returns <tt>True</tt>.  Thus,
    ** to assure that hover feedback remains operational once your
    ** code returns control to the browser, be sure to call
    ** <tt>update()</tt> after making a series of changes to your
    ** chart's properties.
    ** <p>
    **
    ** Understanding how <tt>update</tt> impacts visibility and size:
    ** <p>
    ** <blockquote>
    ** <small>
    ** Due to an implementation-related limitation,
    ** <tt>visibility: hidden</tt> won't hide a GChart
    ** (<tt>update</tt>
    ** commandeers the visibility attribute).  Instead use
    ** <tt>display: none</tt> or, equivalently:
    **
    ** <pre>
    **    myGChart.setVisible(False)
    ** </pre>
    **
    ** If you need to avoid <tt>display: none</tt> (it can change
    ** page layout), you can also hide a GChart via lines such as:
    **
    ** <pre>
    **    DOM.setStyleAttribute(myGChart.getElement(),"overflow","hidden")
    **    myGChart.setPixelSize(0, 0)
    ** </pre>
    **
    ** This later approach gives you the option of leaving the top
    ** corner of the GChart visible, etc. Note that, with the next
    ** <tt>update</tt>, GChart will overwrite your size (based on the
    ** GChart properties that define the size of the the chart, such
    ** as <tt>setChartSize</tt> and <tt>set*Thickness</tt>)
    ** and your <tt>overflow:hidden</tt> (based on
    ** <tt>setClipToDecoratedChart</tt>) specifications. To preserve
    ** them (or in other special cases) you may need to apply such
    ** settings to an enclosing parent element.
    **
    ** </small>
    ** </blockquote>
    **
    **
    ** @param option determines how the touched (or "hovered
    ** over") point changes as a result of this update. See
    ** <tt>TouchedPointUpdateOption</tt> for the available
    ** choices.
    **
    ** @see TouchedPointUpdateOption TouchedPointUpdateOption
    ** @see #setOptimizeForMemory setOptimizeForMemory
    ** @see #isUpdateNeeded isUpdateNeeded
    **
    *"""
    def update(self, option):

        """
        * This method defines each curve's default pie slice
        * orientations, and also separates each curve's points
        * into the vertically or horizontally banded bins,
        * that GChart needs to perform the hit testing
        * that allows it to emulate "touching" points with
        * the mouse.
        * <p>
        *
        * Therefore, this line must come first.
        *
        """
        assembleChart()

        if TouchedPointUpdateOption.TOUCHED_POINT_LOCKED == option:
            # must re-touch (point position, hover-config can change)
            self.plotPanel.touch(self.plotPanel.touchedPoint)

        elif TouchedPointUpdateOption.TOUCHED_POINT_CLEARED == option:
            # if needed, will clear out touched point & related feedback
            self.plotPanel.touch(None)

        elif TouchedPointUpdateOption.TOUCHED_POINT_UPDATED == option:
            # re-determine which point is underneath the mouse now...
            self.plotPanel.retouchObjectAtMousePosition()


        """
        * Because hover feedback curves come at the end of the curve
        * list, given how GChart's rendering process works, this
        * second call only has to update these hover feedback curves
        * (so it's not like we are really building the chart twice)
        *
        """
        assembleChart()



    """*
    * Updates the chart, using an appropriate default touched point
    * update option, depending on if hover touching is enabled or
    * not.<p>
    *
    * A convenience method equivalent to:
    * <p>
    *
    * <pre>
    if getHoverTouchingEnabled():
        update(TouchedPointUpdateOption.TOUCHED_POINT_UPDATED)

    else:
        update(TouchedPointUpdateOption.TOUCHED_POINT_LOCKED)

    * </pre>
    *
    *
    * @see #update(TouchedPointUpdateOption) update(TouchedPointUpdateOption)
    * @see #setHoverTouchingEnabled setHoverTouchingEnabled
    *
    """
    def update(self):
        if getHoverTouchingEnabled():
            update(TouchedPointUpdateOption.TOUCHED_POINT_UPDATED)

        else:
            update(TouchedPointUpdateOption.TOUCHED_POINT_LOCKED)



    # constructs the chart within the chart panel from current specs
    def assembleChart(self):

        if self.chartDecorationsChanged  or  xAxis.limitsChanged()  or  yAxis.limitsChanged()  or  y2Axis.limitsChanged():
            self.plotPanel.reset(xChartSize, yChartSize,
            hasYAxis(), hasY2Axis(),
            xAxis, yAxis, y2Axis)
            GChart.setFontFamily(this,getFontFamily())
            GChart.setBackgroundColor(this, getBackgroundColor())
            GChart.setBorderColor(this, getBorderColor())
            GChart.setBorderStyle(this,getBorderStyle())
            GChart.setBorderWidth(this, getBorderWidth())
            GChart.setPadding(this,getPadding())
            GChart.setOverflow(this, (getClipToDecoratedChart() and
                                        "hidden" or "visible"))

            self.setPixelSize(self.plotPanel.getXChartSizeDecoratedQuickly(),
            self.plotPanel.getYChartSizeDecoratedQuickly())
            updateDecorations(self.plotPanel.getXChartSizeDecoratedQuickly())
            xAxis.rememberLimits()
            yAxis.rememberLimits()
            y2Axis.rememberLimits()
            invalidateEveryCurve()
            self.chartDecorationsChanged = False

        # actually renders chart, including internal curves used
        # to represent the decorations (title, axis labels, etc.)
        realizePlotPanel()

        # To avoid order-of-magnitude FF2 performance hit on busy pages,
        # first time, must add plotPanel only AFTER building chart
        if self.plotPanel != self.chartPanel.getWidget():
            self.chartPanel.add(self.plotPanel)
            """
            * Due to how GChart plays around with visible elements contained inside
            * hidden elements to align it's labels properly, if we allowed top
            * level <tt>visibility:hidden</tt> the result would be that everything
            * <i>except</i> annotations would be invisible.
            * <p>
            *
            * We can prevent such
            * weird behavior by setting <tt>visibility:visible</tt> on the top
            * level element; this setting effectively short-circuits any
            * top level visibility setting the user may have made. <p>
            *
            * Users must either use <tt>display:none</tt> (as the Widget method
            * <tt>setVisible</tt> does) or create an enclosing 0-sized div with
            * <tt>overflow:hidden</tt>) to hide a GChart.
            * <p>
            *
            """
            DOM.setStyleAttribute(getElement(), "visibility","visible")

        else:
            """
            * Without these 2 lines IE7 won't repaint GChart's annotations.
            * The lines are not needed in FF2; an IE7 bug is suspected.<p>
            *
            * I got this workaround from <a href=
            * "http:#examples.roughian.com">Ian Bambury</a> as part of <a
            * href="http:#groups.google.com/group/Google-Web-Toolkit/browse_thread/thread/4c54d8b4aea7f98b/6efd1ab4e5fc0e7b?#6efd1ab4e5fc0e7b">
            * this discussion on the GWT forum</a>.
            * <p>
            *
            * (Note comment regarding need for explicit visibility above).
            *
            """
            DOM.setStyleAttribute(getElement(), "visibility","hidden")
            DOM.setStyleAttribute(getElement(), "visibility","visible")



    # create a Grid representing the chart legend.
    def createLegend(self, pp):
        result = Grid(getNVisibleCurvesOnLegend(), 2)
        iVisible = 0
        """
        * Simply eliminating the border entirely is a valid transparency
        * emulation for the legend (no positional shifting is needed as is
        * needed for the images used to draw the main chart's curves) because
        * the legend is always positioned by its center point, and the border
        * extends around the entire legend key, so removing it does not result
        * in any change to the legend key's center position.  <p>
        *
        * If multiple legend locations (beyond the current "always centered in
        * a band along the right edge" option) were ever supported, appropriate
        * positional shifts would then have to be introduced to emulate
        * transparent borders.
        *
        """
        if TRANSPARENT_BORDER_COLOR == getLegendBorderColor():
            GChart.setBorderWidth(result, 0)
            GChart.setBorderColor(result, "transparent")
        else:
            GChart.setBorderWidth(result, Math.abs(getLegendBorderWidth()))
            GChart.setBorderColor(result, getLegendBorderColor())
        GChart.setBorderStyle(result, getLegendBorderStyle())
        GChart.setBackgroundColor(result, getLegendBackgroundColor())
        nCurves = self.getNCurves()
        for i in range(nCurves):
            c = getSystemCurve(i)
            if c.isVisible()  and  c.getLegendLabel()!=None:
                symBorderFraction = (c.getSymbol().getBorderWidth()/
                                Math.max(
                                Math.max(1.0,c.getSymbol().getFillThickness()),
                                Math.max(c.getSymbol().getWidth(pp),
                                c.getSymbol().getHeight(pp, c.onY2()))))
                icon = c.getSymbol().getSymbolType().createIconImage(
                                        c.getSymbol(), getLegendFontSize(),
                                        symBorderFraction)

                result.setWidget(iVisible, 0, icon)
                result.getCellFormatter().setAlignment(iVisible, 0,
                                        HasHorizontalAlignment.ALIGN_CENTER,
                                        HasVerticalAlignment.ALIGN_MIDDLE)

                label = HTML(c.getLegendLabel())
                GChart.setFontWeight(label, getLegendFontWeight())
                GChart.setFontStyle(label, getLegendFontStyle())
                GChart.setColor(label, getLegendFontColor())
                GChart.setFontSize(label, getLegendFontSize())

                result.setWidget(iVisible, 1, label)
                result.getCellFormatter().setAlignment(iVisible, 1,
                                        HasHorizontalAlignment.ALIGN_LEFT,
                                        HasVerticalAlignment.ALIGN_MIDDLE)

                iVisible += 1


        return result


    # returns char-width-based default legend thickness
    def getDefaultLegendThickness(self):
        EXTRA_WIDTH = 5;  # allow for padding & symbol
        maxLen = 0
        nCurves = self.getNCurves()
        for i in range(nCurves):
            c = getSystemCurve(i)
            if c.isVisible()  and  None != c.getLegendLabel():
                maxLen = Math.max(maxLen,
                htmlWidth(c.getLegendLabel()))


        return int ( ((maxLen + EXTRA_WIDTH) *
                        getLegendFontSize() *
                        TICK_CHARWIDTH_TO_FONTSIZE_LOWERBOUND))


    def getNVisibleCurvesOnLegend(self):
        result = 0
        nCurves = self.getNCurves()
        for i in range(nCurves):
            if getSystemCurve(i).isVisible()  and  getSystemCurve(i).getLegendLabel() is not None:
                result += 1

        return result


    # Defines a default curve border color when curves first created
    def setDefaultBorderColor(self, curve, index):
        curve.getSymbol().setBorderColor(
                    self.defaultSymbolBorderColors[
                                    index % len(self.defaultSymbolBorderColors)
                                ])



    # renders the curve in the plot panel
    def realizeCurve(self, c):
        if not c.isValidated():
            internalIndex = getInternalCurveIndex(c)
            rpIndex = getRenderingPanelIndex(internalIndex)
            grp = self.plotPanel.getGraphicsRenderingPanel(rpIndex)
            arp = self.plotPanel.getAnnotationRenderingPanel(rpIndex)
            if PlotPanel.DECORATIVE_RENDERING_PANEL_INDEX == rpIndex:
                # background panel only gets initialized for first curve
                if 0 == internalIndex:
                    # background panel never uses canvas
                    grp.beginRendering(None)
                    arp.beginRendering()

                c.setWasCanvasRendered(False)

            # continuous fill# non-empty fill# canvas available
            elif 0 == c.getSymbol().getFillSpacing()  and  0 < c.getSymbol().getFillThickness()  and  None != getCanvasFactory()  and            c.isVisible():
                grp.maybeAddCanvas()
                canvasRegion = c.getContainingRectangle(self.plotPanel)
                grp.beginRendering(canvasRegion)
                arp.beginRendering()
                c.setWasCanvasRendered(True)

            else:
                # does not use canvas, or it is invisible
                grp.beginRendering(None)
                arp.beginRendering()
                c.setWasCanvasRendered(False)


            if c.isVisible():
                # Separate points into vertical/horizontal band-bins provided
                # 1) it is not a system curve and 2) it is not of a type whose
                # position follows the mouse (and thus has no fixed location
                # suitable for banding) and 3) at least one kind of hover feedback
                # is being provided for the curve.
                if getCurveIndex(c) >= 0  and  not isMouseAnchored(c.getSymbol().getSymbolType())  and  (c.getSymbol().getHoverSelectionEnabled()  or  c.getSymbol().getHoverAnnotationEnabled()):
                    c.bandSeparatePoints()

                else:
                    # hit test banding calcs unneeded; skip them for speed.
                    c.clearBandList()

                # Note: these lines must come AFTER band separation lines above
                nPoints = c.getNPoints()
                for j in range(nPoints):
                    c.realizePoint(self.plotPanel, grp, arp, j)


            # only end background panel rendering w last background curve
            if PlotPanel.DECORATIVE_RENDERING_PANEL_INDEX != rpIndex  or  internalIndex == N_PRE_SYSTEM_CURVES-1:
                grp.endRendering()
                arp.endRendering()

            # else it's a background panel curve, and not the last one

            c.isValidated = True



    # marks every curve, including system curves, as needing an update
    def invalidateEveryCurve(self):
        for i in range(len(self.curves)):
            self.curves.get(i).invalidate()


    # marks every developer-accessible curve as needing an update
    def invalidateAccessibleCurves(self):
        nCurves = self.getNCurves()
        for i in range(nCurves):
            getSystemCurve(i).invalidate()



    # invalidates every curve that has a pie slice type
    def invalidateAllSlices(self):
        nCurves = self.getNCurves()
        for i in range(nCurves):
            c = getSystemCurve(i)
            if isinstance(c.getSymbol().getSymbolType(),
                          SymbolType.PieSliceSymbolType):
                c.invalidate()



    # Invalidates every pie slice curve whose orientation could
    # depend on the orientation of the given curve
    def invalidateDependentSlices(self, iFirstCurve):
        # only user defined curve can have slice dependency relationships
        if isSystemCurveIndex(iFirstCurve):
            return

        nCurves = self.getNCurves()
        for i in range(iFirstCurve, nCurves):
            c = getSystemCurve(i)
            if isinstance(c.getSymbol().getSymbolType(),
                          SymbolType.PieSliceSymbolType):
                c.invalidate()

            elif i == iFirstCurve:
                # if first curve isn't a slice,
                break;                  # there are no dependent slices




    # Defines the default pie slice orientations for every pie-slice curve
    def setDefaultPieSliceOrientations(self):
        setLastPieSliceOrientation(getInitialPieSliceOrientation())
        nCurves = self.getNCurves()
        for i in range(nCurves):
            c = getSystemCurve(i)
            # keep track of default next orientation for pie slices
            # (must do this even if we don't have to redraw slice)
            if isinstance(c.getSymbol().getSymbolType(),
                            SymbolType.PieSliceSymbolType):
                c.getSymbol().setDefaultPieSliceOrientation(
                getLastPieSliceOrientation())
                setLastPieSliceOrientation(
                c.getSymbol().getDecodedPieSliceOrientation()
                + c.getSymbol().getPieSliceSize())





    def realizePlotPanel(self):

        setDefaultPieSliceOrientations()
        """
        * Render both system curves (those with negative ids that
        * are used to render title, ticks, etc.) and ordinary curves.
        """
        nCurves = self.getNCurves()
        for i in range(-N_SYSTEM_CURVES, nCurves):
            c = getSystemCurve(i)
            self.realizeCurve(c)




    """ Returns True if the rendering panel index is associated
    * with one of the internal, hover-feedback curves.
    * <p>
    *
    * This method relies on the fact that rendering panels
    * appear in this order:
    * <p>
    *
    * <ol>
    * <li> a single rp that renders all chart decorations
    * <li> self.getNCurves() rps (1 for each developer-defined curve)
    * <li> the two rendering panels associated with the two
    *   system-defined hover feedback curves
    * </ol>
    *
    """
    def isHoverFeedbackRenderingPanel(self, rpIndex):
        result = rpIndex > self.getNCurves()
        return result



    """
    * This code works around a bug in GWTCanvas that can cause
    * (in IE) previously rendered VML elements to have their fill
    * and stroke color, and stroke thickness properties revert to
    * some sort of defaults (I saw white, black, and 1px in my
    * tests) when the canvas is re-inserted into the DOM.
    *
    * See TestGChart55.java and TestGChart55a.java for more
    * info on the GWTCanvas bug that makes this code neccessary.
    *
    * TODO: Implement technique of GWTCanvasIssue293.patch to
    * override removeFromParent and store/restore innerHTML
    * as a more efficient workaround for this problem. If
    * a GWTCanvas is released, you could remove this
    * workaround altogether.
    *
    """

    # avoids inefficiency of re-rendering in most common case
    def onUnload(self):
        Composite.onUnload(self)
        self.wasUnloaded = True


    def onLoad(self):
        Composite.onLoad(self)
        if self.wasUnloaded  and  self.plotPanel.getRenderingPanelCount() > 0:
            isUpToDate = not isUpdateNeeded()
            nCurves = self.getNCurves()
            for i in range(nCurves):
                c = getCurve(i)
                if c.isCanvasRendered():
                    c.invalidate()
                    if isUpToDate:
                        self.realizeCurve(c)

                    # else since chart needs update, presume they will
                    # update later, no need to auto-patch things up
                    # (and simple patch-rerender won't work anyway).


        # else never inserted/rendered; skip patchup-rerendering


 # end of class GChart
