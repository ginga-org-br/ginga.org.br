---
title: "Element &lt;regionBase&gt;"
---

### Definition and Usage { data-search-exclude }

The [&lt;regionBase&gt;](regionbase.md) element groups a set of [&lt;region&gt;](region.md) elements, each
of which may contain another set of nested [&lt;region&gt;](region.md) elements, and so
on, recursively.

Each [&lt;regionBase&gt;](regionbase.md) element is associated with a class of devices where
presentation will take place.  To identify the association, the
[&lt;regionBase&gt;](regionbase.md) element defines the *device* attribute.  When the
attribute is not specified, the presentation takes place in the same device
that runs the NCL player.

There are two different types of device classes: active and passive.  In an
active class, a device is able to run some media players for [&lt;media&gt;](media.md)
element presentations.  In a passive class, a device is not required to run
media players, only to exhibit a bit map or a sequence of audio samples
received from another device.

The "deviceClass" property of a [&lt;media&gt;](media.md) element is initialized with the
*device* value, if the [&lt;media&gt;](media.md) element indirectly refers to a
[&lt;region&gt;](region.md) element inside a [&lt;regionBase&gt;](regionbase.md), by using a
[&lt;descriptor&gt;](descriptor.md) element.

The chosen class also defines the global environment variables (properties
of the settings object ---[&lt;media&gt;](media.md) element of
"application/x-ncl-settings" type): "system.screenSize(i)",
"system.screenGraphicSize(i)", and "system.audioType(i)".

The "systemScreen(1)" and "systemAudio(1)" are reserved to passive classes,
and "systemScreen(2)" and "systemAudio(2)" are reserved to active classes.

The [&lt;regionBase&gt;](regionbase.md) element that defines a passive class may also have a
region attribute.  This attribute is used to identify a [&lt;region&gt;](region.md)
element in another [&lt;regionBase&gt;](regionbase.md) associated with the parent device that
creates the bit map sent to the passive class; in the specified region the
bit map must also be exhibited.  The "system.parentDeviceRegion(i)" property
of the settings object ([&lt;media&gt;](media.md) element of "application/x-ncl-settings"
type) is initialized with the *region* attribute value.

### Syntax { data-search-exclude }

| Element | Attributes | Content | Parent |  |
| --- | --- | --- | --- | --- |
| [&lt;regionBase&gt;](regionbase.md) | *id*, *device*, *region* | ([&lt;importBase&gt;](importbase.md) | [&lt;region&gt;](region.md))+ | [&lt;head&gt;](head.md) |

### Attributes { data-search-exclude }

| Name | Value | Description |
| --- | --- | --- |
| *id* | It may receive any string value that begins with a letter or an underscore and that only contains letters, digits, <".">, and <"_">. | The *id* attribute uniquely identifies the element within a document. |
| *device* | "systemScreen(i)" or "systemAudio(i)".  Where the attribute is not specified, the presentation shall take place in the same device class that runs the NCL player. | The *device* attribute identifies the class of devices where presentation will take place. |
| *region* | IDREF. | The *region* attribute identify a [&lt;region&gt;](region.md) element in another [&lt;regionBase&gt;](regionbase.md) associated with the parent device that creates the bit map sent to the passive class; in the specified region the bitmap must also be exhibited. |
