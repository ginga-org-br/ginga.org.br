---
title: "Element &lt;transition&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;transition&gt;](transition.md) element allows for defining a transition template.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |
| --- | --- | --- | --- |
| [&lt;transition&gt;](transition.md) | <u>*id*</u>, <u>*type*</u>, *subtype*, *dur*, *startProgress*, *endProgress*, *direction*, *fadeColor*, *horzRepeat*, *vertRepeat*, *borderWidth*, *borderColor* | -- | [&lt;transitionBase&gt;](transitionbase.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *type* | "barWipe", "irisWipe", "clockWipe", "snakeWipe", or "fade".  These are the required values.  For the complete list of predefined transition types see: http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix. | The *type* and *subtype* attributes define the transition. |
| *subtype* | The required subtype values depend on the type value.  For "barWipe" the required subtype is "leftToRight", for "irisWipe" it is "rectangle", for "clockWipe" it is "clockwiseTwelve", for "snakeWipe" it is "topLeftHorizontal", and for "fade" it is "crossfade".  The complete list can be found at http://www.w3.org/TR/SMIL2/smil-transitions.html#TransitionEffects-Appendix.  The required subtype values are also the default values. | The *type* and *subtype* attributes define the transition. |
| *dur* | The *dur* attribute is specified according with one of the following syntax: (i) "Hours:Minutes:Seconds.Fraction", where "Hours" is an integer in the \[0,23\] interval, "Minutes" is an integer in the \[0,59\] interval, "Minutes" is an integer in the \[0,59\] interval, and "Fraction" is a positive integer; (ii) Seconds<"s">, where "Seconds" is a positive real number.  The default value is "1s". | The *dur* attribute specifies the duration of the transition. |
| *startProgress* | A real number in the range \[0,1\].  The default value is 0. | The *startProgress* attribute specifies the amount of progress through the transition at which to begin execution. For instance, we may want to begin a crossfade with the destination image being already 30% faded in.  For this case, *startProgress* would be 0.3. |
| *endProgress* | A real number in the range \[0,1\].  The default value is 0. | The *endProgress* attribute specifies the amount of progress through the transition at which to end execution.  The value of this attribute shall be greater than or equal to the value of the *startProgress* attribute. If *endProgress* is equal to *startProgress*, then the transition remains at a fixed progress for the duration of the transition. |
| *direction* | "forward" or "backward".  The default value is "forward". | Specifies the direction the transition will run.  Note that not all transitions will have meaningful reverse interpretations.  For instance, a crossfade is not a geometric transition, and therefore has no interpretation of reverse direction. Transitions that do not have a reverse interpretation have their direction attribute ignored and the default value of "forward" is assumed. |
| *fadeColor* | "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua", or "teal".  The default value is "black". | If the value of the *type* attribute is "fade" and the value of the *subtype* attribute is "fadeToColor" or "fadeFromColor", then the *fadeColor* attribute specifies the ending or starting color of the fade. If the value of the *type* attribute is not "fade", or the value of the *subtype* attribute is not "fadeToColor" or "fadeFromColor", then the *fadeColor* attribute shall be ignored. |
| *horzRepeat* | Positive integer.  The default value is 1. | This attribute is valid only if the value of the *type* attribute is not "fade".  It specifies how many times to perform the transition pattern along the horizontal axis. |
| *vertRepeat* | Positive integer.  The default value is 1. | This attribute is valid only if the value of the *type* attribute is not "fade".  It specifies how many times to perform the transition pattern along the vertical axis. |
| *borderWidth* | Positive integer.  The default value is 0. | This attribute is valid only if the value of the *type* attribute is not "fade".  It specifies the width of a generated border along a wipe edge. |
| *borderColor* | "white", "black", "silver", "gray", "red", "maroon", "fuchsia", "purple", "lime", "green", "yellow", "olive", "blue", "navy", "aqua", or "teal".  The default value is "black". | This attribute is valid only if the value of the type attribute is not "fade".  It specifies the content of the generated border along a wipe edge. If the value of this attribute is a color, then the generated border along the wipe or warp edge is filled with this color. If the value of this attribute is "blend", then the generated border along the wipe blend is an additive blend (or blur) of the media sources. |
