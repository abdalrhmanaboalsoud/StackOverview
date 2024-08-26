| Category          | Normal CSS                  | Tailwind CSS                | Description                                                            |
|-------------------|-----------------------------|-----------------------------|------------------------------------------------------------------------|
| **Colors**        | `color: red;`               | `text-red-500`              | Sets the text color to red (500 is the shade).                         |
| **Background**    | `background-color: blue;`   | `bg-blue-500`               | Sets the background color to blue (500 is the shade).                  |
| **Padding**       | `padding: 1rem;`            | `p-4`                       | Sets padding on all sides to 1rem (4 is Tailwind's scale unit).        |
| **Margin**        | `margin: 1rem;`             | `m-4`                       | Sets margin on all sides to 1rem (4 is Tailwind's scale unit).         |
| **Flexbox**       | `display: flex;`            | `flex`                      | Applies a flexbox layout to the element.                               |
| **Justify Content**| `justify-content: center;` | `justify-center`            | Centers flexbox items horizontally.                                    |
| **Align Items**   | `align-items: center;`      | `items-center`              | Centers flexbox items vertically.                                      |
| **Width**         | `width: 100%;`              | `w-full`                    | Sets the width to 100%.                                                |
| **Height**        | `height: 100%;`             | `h-full`                    | Sets the height to 100%.                                               |
| **Display**       | `display: block;`           | `block`                     | Sets the element to display as a block.                                |
| **Text Align**    | `text-align: center;`       | `text-center`               | Centers text within the element.                                       |
| **Font Size**     | `font-size: 16px;`          | `text-base`                 | Sets the font size to 16px.                                            |
| **Border**        | `border: 1px solid black;`  | `border border-black`       | Adds a 1px solid black border around the element.                      |
| **Border Radius** | `border-radius: 0.25rem;`   | `rounded`                   | Applies a small border radius (0.25rem) to the element.                |
| **Shadow**        | `box-shadow: 0px 4px 6px;`  | `shadow-lg`                 | Applies a large shadow to the element.                                 |
| **Opacity**       | `opacity: 0.5;`             | `opacity-50`                | Sets the opacity of the element to 50%.                                |
| **Overflow**      | `overflow: hidden;`         | `overflow-hidden`           | Hides overflow content that extends beyond the element's bounds.       |
| **Z-Index**       | `z-index: 10;`              | `z-10`                      | Sets the z-index to 10, determining the stack order of the element.    |
| **Font Weight**   | `font-weight: bold;`        | `font-bold`                 | Sets the font weight to bold.                                          |
| **Line Height**   | `line-height: 1.5;`         | `leading-relaxed`           | Sets a relaxed line height for text (1.5).                             |
| **Letter Spacing**| `letter-spacing: 0.1rem;`   | `tracking-wide`             | Increases the letter spacing for text.                                 |
| **Grid Layout**   | `display: grid;`            | `grid`                      | Applies a grid layout to the element.                                  |
| **Grid Columns**  | `grid-template-columns: 1fr 2fr;` | `grid-cols-3`        | Defines a grid with 3 equal columns.                                   |
| **Grid Rows**     | `grid-template-rows: auto;` | `grid-rows-1`               | Defines a grid with 1 row.                                             |
| **Position**      | `position: absolute;`       | `absolute`                  | Sets the element's position to absolute.                               |
| **Top/Right/Bottom/Left** | `top: 0;`           | `top-0`                     | Positions the element 0 units from the top.                            |
| **Cursor**        | `cursor: pointer;`          | `cursor-pointer`            | Changes the cursor to a pointer on hover.                              |
| **Visibility**    | `visibility: hidden;`       | `invisible`                 | Hides the element, but it still occupies space.                        |
| **Font Family**   | `font-family: Arial, sans-serif;` | `font-sans`          | Applies a sans-serif font family.                                      |
| **Text Transform**| `text-transform: uppercase;` | `uppercase`              | Transforms text to uppercase.                                          |
| **List Style**    | `list-style-type: none;`    | `list-none`                 | Removes list bullets.                                                  |
| **Transition**    | `transition: all 0.3s ease;`| `transition-all`            | Applies a smooth transition effect to all properties.                  |
| **Transform**     | `transform: scale(1.5);`    | `scale-150`                 | Scales the element to 1.5 times its original size.                     |
| **Rotate**        | `transform: rotate(45deg);` | `rotate-45`                 | Rotates the element by 45 degrees.                                     |
| **Translate**     | `transform: translateX(10px);` | `translate-x-10`        | Moves the element 10px to the right.                                   |
| **Skew**          | `transform: skewX(20deg);`  | `skew-x-20`                 | Skews the element 20 degrees along the X-axis.                         |
| **Object Fit**    | `object-fit: cover;`        | `object-cover`              | Scales an image to cover its container.                                |
| **Object Position**| `object-position: center;` | `object-center`             | Centers an image within its container.                                 |
| **Appearance**    | `appearance: none;`         | `appearance-none`           | Removes default styling of form elements.                              |
| **Place Items**   | `place-items: center;`      | `place-items-center`        | Centers items in both axes in a grid or flex container.                |
| **Resize**        | `resize: vertical;`         | `resize-y`                  | Allows vertical resizing of a textarea.                                |
| **Select None**   | `user-select: none;`        | `select-none`               | Prevents text selection by the user.                                   |
| **Pointer Events**| `pointer-events: none;`     | `pointer-events-none`       | Disables pointer events on an element.                                 |
| **Align Self**    | `align-self: flex-start;`   | `self-start`                | Aligns a flexbox child element at the start of the flex container.     |
| **Aspect Ratio**  | `aspect-ratio: 16/9;`       | `aspect-w-16 aspect-h-9`    | Sets a 16:9 aspect ratio for an element.                               |
| **Scroll Behavior** | `scroll-behavior: smooth;` | `scroll-smooth`           | Enables smooth scrolling for anchor links.                             |
| **Stroke Width**  | `stroke-width: 2;`          | `stroke-2`                  | Sets the stroke width of SVG elements.                                 |
| **Fill**          | `fill: currentColor;`       | `fill-current`              | Sets the fill color of SVG elements to the current text color.         |
| **Gap**           | `gap: 1rem;`                | `gap-4`                     | Sets a gap between grid or flexbox items.                              |
| **Grid Auto Rows** | `grid-auto-rows: minmax(100px, auto);` | `auto-rows-min` | Defines the size of implicitly created grid rows.                     |
| **Backdrop Blur** | `backdrop-filter: blur(5px);` | `backdrop-blur-sm`       | Applies a small blur effect to the backdrop of an element.             |
| **Backdrop Brightness** | `backdrop-filter: brightness(150%);` | `backdrop-brightness-150` | Increases the brightness of the backdrop.              |
| **Backdrop Contrast** | `backdrop-filter: contrast(125%);` | `backdrop-contrast-125` | Increases the contrast of the backdrop.              |
| **Backdrop Grayscale** | `backdrop-filter: grayscale(100%);` | `backdrop-grayscale` | Converts the backdrop to grayscale.              |
| **Backdrop Hue Rotate** | `backdrop-filter: hue-rotate(90deg);` | `backdrop-hue-rotate-90` | Rotates the hue of the backdrop by 90 degrees.              |
| **Backdrop Invert** | `backdrop-filter: invert(100%);` | `backdrop-invert` | Inverts the backdrop colors.              |
| **Backdrop Opacity** | `backdrop-filter: opacity(50%);` | `backdrop-opacity-50` | Sets the opacity of the backdrop to 50%.              |
| **Backdrop Saturate** | `backdrop-filter: saturate(150%);` | `backdrop-saturate-150` | Increases the saturation of the backdrop.              |
| **Backdrop Sepia** | `backdrop-filter: sepia(100%);` | `backdrop-sepia` | Converts the backdrop to sepia.              |
| **Ring Width**  | `outline-width: 2px;` | `ring-2` | Sets the ring (outline) width around an element to 2px.              |
| **Ring Color**  | `outline-color: #000;` | `ring-black` | Sets the ring (outline) color to black.              |
| **Ring Offset Width**  | `outline-offset: 2px;` | `ring-offset-2` | Sets the offset of the ring (outline) around an element.              |
| **Ring Offset Color**  | `outline-color: #fff;` | `ring-offset-white` | Sets the offset color of the ring (outline) around an element to white.              |
| **Backface Visibility**  | `backface-visibility: hidden;` | `backface-hidden` | Hides the backface of an element during 3D transforms.              |
| **Break After**  | `break-after: avoid;` | `break-after-avoid` | Prevents the element from being broken after a page break.              |
| **Break Before**  | `break-before: avoid;` | `break-before-avoid` | Prevents the element from being broken before a page break.              |
| **Break Inside**  | `break-inside: avoid;` | `break-inside-avoid` | Prevents the element from being broken inside a page break.              |
| **Box Decoration Break**  | `box-decoration-break: slice;` | `decoration-slice` | Specifies how an element's decoration should behave when broken across lines or pages.              |
| **Background Clip**  | `background-clip: border-box;` | `bg-clip-border` | Clips the background to the border box.              |
| **Background Origin**  | `background-origin: padding-box;` | `bg-origin-padding` | Sets the origin of the background to the padding box.              |
| **Column Count**  | `column-count: 3;` | `columns-3` | Specifies the number of columns an element should be divided into.              |
| **Column Span**  | `column-span: all;` | `col-span-full` | Specifies that the element should span across all columns.              |
| **Caret Color**  | `caret-color: red;` | `caret-red-500` | Sets the color of the text caret (cursor).              |
| **Content Visibility**  | `content-visibility: auto;` | `content-auto` | Specifies that the element's visibility should be optimized for performance.              |
| **Scroll Margin Top**  | `scroll-margin-top: 1rem;` | `scroll-mt-4` | Sets the margin of an element before a scroll snap position at the top of the container.              |
| **Scroll Margin Right**  | `scroll-margin-right: 1rem;` | `scroll-mr-4` | Sets the margin of an element before a scroll snap position at the right of the container.              |
| **Scroll Margin Bottom**  | `scroll-margin-bottom: 1rem;` | `scroll-mb-4` | Sets the margin of an element before a scroll snap position at the bottom of the container.              |
| **Scroll Margin Left**  | `scroll-margin-left: 1rem;` | `scroll-ml-4` | Sets the margin of an element before a scroll snap position at the left of the container.              |
| **Scroll Padding Top**  | `scroll-padding-top: 1rem;` | `scroll-pt-4` | Sets the padding of an element after a scroll snap position at the top of the container.              |
| **Scroll Padding Right**  | `scroll-padding-right: 1rem;` | `scroll-pr-4` | Sets the padding of an element after a scroll snap position at the right of the container.              |
| **Scroll Padding Bottom**  | `scroll-padding-bottom: 1rem;` | `scroll-pb-4` | Sets the padding of an element after a scroll snap position at the bottom of the container.              |
| **Scroll Padding Left**  | `scroll-padding-left: 1rem;` | `scroll-pl-4` | Sets the padding of an element after a scroll snap position at the left of the container.              |
| **Scroll Snap Align**  | `scroll-snap-align: start;` | `snap-start` | Specifies that the element should align with the start of the scroll container.              |
| **Scroll Snap Stop**  | `scroll-snap-stop: always;` | `snap-always` | Specifies that the element should stop at the snap position in the scroll container.              |
| **px**     | `width: 100px;`     | `w-[100px]`          | Sets width to 100 pixels.                             |
| **rem**    | `padding: 1rem;`    | `p-4`                | Sets padding using rem units (1 rem ≈ 16px).          |
| **em**     | `font-size: 1.5em;` | `text-[1.5em]`       | Sets font size to 1.5 times the current font size.    |
| **%**      | `width: 50%;`       | `w-1/2`              | Sets width to 50 percent of the parent element.       |
| **vh**     | `height: 100vh;`    | `h-screen`           | Sets height to 100% of the viewport height.           |
| **vw**     | `width: 100vw;`     | `w-screen`           | Sets width to 100% of the viewport width.             |
| **fr**     | `grid-template-columns: 1fr 2fr;` | `grid-cols-[1fr 2fr]` | Defines a grid with fractional units. |
| **deg**    | `transform: rotate(45deg);` | `rotate-45` | Rotates the element by 45 degrees.                   |
| **s**      | `transition-duration: 0.5s;` | `duration-500` | Sets transition duration to 0.5 seconds.            |
| **ms**     | `animation-duration: 200ms;` | `duration-[200ms]` | Sets animation duration to 200 milliseconds.         |
| **%**      | `opacity: 50%;`     | `opacity-50`         | Sets opacity to 50%.                                  |
| **pt**     | `font-size: 12pt;`  | `text-[12pt]`        | Sets font size to 12 points.
| **Responsive Z-index**      | `z-index: 1;`                                    | `z-10`                          | Sets z-index to 10 for all screen sizes.         |
|                             | `@media (min-width: 640px) { z-index: 20; }`     | `sm:z-20`                       | Sets z-index to 20 on small screens and up.     |
|                             | `@media (min-width: 768px) { z-index: 30; }`     | `md:z-30`                       | Sets z-index to 30 on medium screens and up.    |
| **Responsive Border Width** | `border-width: 1px;`                             | `border`                        | Sets border width to 1px for all screen sizes.   |
|                             | `@media (min-width: 640px) { border-width: 2px; }` | `sm:border-2`                  | Sets border width to 2px on small screens and up.|
|                             | `@media (min-width: 768px) { border-width: 4px; }` | `md:border-4`                  | Sets border width to 4px on medium screens and up.|
| **Responsive Border Color** | `border-color: #000;`                            | `border-black`                  | Sets border color to black for all screen sizes. |
|                             | `@media (min-width: 640px) { border-color: #333; }` | `sm:border-gray-700`          | Sets border color to gray-700 on small screens and up.|
|                             | `@media (min-width: 768px) { border-color: #666; }` | `md:border-gray-600`          | Sets border color to gray-600 on medium screens and up.|
| **Responsive Border Radius**| `border-radius: 4px;`                            | `rounded-sm`                    | Sets border radius to 4px for all screen sizes.  |
|                             | `@media (min-width: 640px) { border-radius: 8px; }` | `sm:rounded-md`               | Sets border radius to 8px on small screens and up.|
|                             | `@media (min-width: 768px) { border-radius: 16px; }` | `md:rounded-lg`               | Sets border radius to 16px on medium screens and up.|
| **Responsive Box Shadow**   | `box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);`     | `shadow-sm`                     | Applies a small box shadow for all screen sizes. |
|                             | `@media (min-width: 640px) { box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }` | `sm:shadow-md`                 | Applies a medium box shadow on small screens and up.|
|                             | `@media (min-width: 768px) { box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1); }` | `md:shadow-lg`                | Applies a large box shadow on medium screens and up.|
| **Responsive Opacity**      | `opacity: 1;`                                    | `opacity-100`                   | Sets opacity to 100% for all screen sizes.      |
|                             | `@media (min-width: 640px) { opacity: 0.75; }`   | `sm:opacity-75`                 | Sets opacity to 75% on small screens and up.    |
|                             | `@media (min-width: 768px) { opacity: 0.5; }`    | `md:opacity-50`                 | Sets opacity to 50% on medium screens and up.   |
| **Responsive Filter**       | `filter: blur(0px);`                             | `filter`                        | Applies no blur filter for all screen sizes.     |
|                             | `@media (min-width: 640px) { filter: blur(4px); }` | `sm:blur-sm`                   | Applies a small blur filter on small screens and up.|
|                             | `@media (min-width: 768px) { filter: blur(8px); }` | `md:blur-md`                   | Applies a medium blur filter on medium screens and up.|
| **Responsive Transition**   | `transition: all 0.3s ease;`                     | `transition-all`                | Applies a smooth transition to all properties for all screen sizes. |
|                             | `@media (min-width: 640px) { transition: opacity 0.5s ease; }` | `sm:transition-opacity`      | Applies a transition to opacity on small screens and up.|
|                             | `@media (min-width: 768px) { transition: transform 0.7s ease; }` | `md:transition-transform` | Applies a transition to transform on medium screens and up.|
| **Responsive Cursor**       | `cursor: auto;`                                 | `cursor-auto`                   | Sets cursor to auto for all screen sizes.       |
|                             | `@media (min-width: 640px) { cursor: pointer; }`  | `sm:cursor-pointer`            | Sets cursor to pointer on small screens and up. |
|                             | `@media (min-width: 768px) { cursor: crosshair; }` | `md:cursor-crosshair`         | Sets cursor to crosshair on medium screens and up. |
| **Responsive Overflow**     | `overflow: auto;`                               | `overflow-auto`                 | Sets overflow to auto for all screen sizes.     |
|                             | `@media (min-width: 640px) { overflow: hidden; }` | `sm:overflow-hidden`           | Sets overflow to hidden on small screens and up.|
|                             | `@media (min-width: 768px) { overflow: scroll; }` | `md:overflow-scroll`           | Sets overflow to scroll on medium screens and up.|
| **Responsive Flex Wrap**    | `flex-wrap: nowrap;`                             | `flex-nowrap`                   | Sets flex-wrap to nowrap for all screen sizes.  |
|                             | `@media (min-width: 640px) { flex-wrap: wrap; }` | `sm:flex-wrap`                 | Sets flex-wrap to wrap on small screens and up. |
|                             | `@media (min-width: 768px) { flex-wrap: wrap-reverse; }` | `md:flex-wrap-reverse`      | Sets flex-wrap to wrap-reverse on medium screens and up.|
| **Responsive Flex Grow**    | `flex-grow: 1;`                                  | `flex-grow`                     | Sets flex-grow to 1 for all screen sizes.       |
|                             | `@media (min-width: 640px) { flex-grow: 2; }`    | `sm:flex-grow-2`               | Sets flex-grow to 2 on small screens and up.    |
|                             | `@media (min-width: 768px) { flex-grow: 3; }`    | `md:flex-grow-3`               | Sets flex-grow to 3 on medium screens and up.   |
| **Responsive Flex Shrink**  | `flex-shrink: 1;`                                | `flex-shrink`                   | Sets flex-shrink to 1 for all screen sizes.     |
|                             | `@media (min-width: 640px) { flex-shrink: 2; }`  | `sm:flex-shrink-2`             | Sets flex-shrink to 2 on small screens and up.  |
|                             | `@media (min-width: 768px) { flex-shrink: 3; }`  | `md:flex-shrink-3`             | Sets flex-shrink to 3 on medium screens and up. |
| **Responsive Align Items**  | `align-items: stretch;`                          | `items-stretch`                 | Sets align-items to stretch for all screen sizes.|
|                             | `@media (min-width: 640px) { align-items: center; }` | `sm:items-center`            | Sets align-items to center on small screens and up.|
|                             | `@media (min-width: 768px) { align-items: end; }` | `md:items-end`                | Sets align-items to end on medium screens and up.|
| **Responsive Justify Content** | `justify-content: flex-start;`                  | `justify-start`                 | Sets justify-content to flex-start for all screen sizes. |
|                             | `@media (min-width: 640px) { justify-content: center; }` | `sm:justify-center`         | Sets justify-content to center on small screens and up.|
|                             | `@media (min-width: 768px) { justify-content: end; }` | `md:justify-end`            | Sets justify-content to end on medium screens and up. |
| **Responsive Align Self**   | `align-self: auto;`                              | `self-auto`                     | Sets align-self to auto for all screen sizes.   |
|                             | `@media (min-width: 640px) { align-self: center; }` | `sm:self-center`             | Sets align-self to center on small screens and up.|
|                             | `@media (min-width: 768px) { align-self: end; }` | `md:self-end`                 | Sets align-self to end on medium screens and up.|
| **Responsive Object Fit**   | `object-fit: contain;`                           | `object-contain`                | Sets object-fit to contain for all screen sizes. |
|                             | `@media (min-width: 640px) { object-fit: cover; }` | `sm:object-cover`            | Sets object-fit to cover on small screens and up.|
|                             | `@media (min-width: 768px) { object-fit: fill; }` | `md:object-fill`              | Sets object-fit to fill on medium screens and up.|
| **Responsive Text Align**   | `text-align: left;`                              | `text-left`                     | Sets text-align to left for all screen sizes.   |
|                             | `@media (min-width: 640px) { text-align: center; }` | `sm:text-center`             | Sets text-align to center on small screens and up.|
|                             | `@media (min-width: 768px) { text-align: right; }` | `md:text-right`              | Sets text-align to right on medium screens and up.|
| **Responsive Letter Spacing** | `letter-spacing: normal;`                       | `tracking-normal`               | Sets letter-spacing to normal for all screen sizes. |
|                             | `@media (min-width: 640px) { letter-spacing: 0.5px; }` | `sm:tracking-tight`         | Sets letter-spacing to 0.5px on small screens and up.|
|                             | `@media (min-width: 768px) { letter-spacing: 1px; }` | `md:tracking-wide`          | Sets letter-spacing to 1px on medium screens and up.|
| **Responsive Line Height**  | `line-height: 1.5;`                              | `leading-normal`                | Sets line-height to 1.5 for all screen sizes.   |
|                             | `@media (min-width: 640px) { line-height: 1.75; }` | `sm:leading-relaxed`         | Sets line-height to 1.75 on small screens and up.|
|                             | `@media (min-width: 768px) { line-height: 2; }`  | `md:leading-loose`            | Sets line-height to 2 on medium screens and up. |
| **Responsive Text Decoration** | `text-decoration: none;`                        | `no-underline`                  | Sets text-decoration to none for all screen sizes. |
|                             | `@media (min-width: 640px) { text-decoration: underline; }` | `sm:underline`               | Sets text-decoration to underline on small screens and up.|
|                             | `@media (min-width: 768px) { text-decoration: line-through; }` | `md:line-through`         | Sets text-decoration to line-through on medium screens and up.|
| **Responsive Text Transform** | `text-transform: none;`                        | `uppercase`                     | Sets text-transform to uppercase for all screen sizes. |
|                             | `@media (min-width: 640px) { text-transform: capitalize; }` | `sm:capitalize`             | Sets text-transform to capitalize on small screens and up.|
|                             | `@media (min-width: 768px) { text-transform: lowercase; }` | `md:lowercase`              | Sets text-transform to lowercase on medium screens and up.|
| **Responsive Vertical Align** | `vertical-align: baseline;`                    | `align-baseline`                | Sets vertical-align to baseline for all screen sizes. |
|                             | `@media (min-width: 640px) { vertical-align: top; }` | `sm:align-top`               | Sets vertical-align to top on small screens and up.|
|                             | `@media (min-width: 768px) { vertical-align: bottom; }` | `md:align-bottom`           | Sets vertical-align to bottom on medium screens and up.|
| **Responsive Visibility**   | `display: block;`                               | `block`                         | Sets display to block for all screen sizes.     |
|                             | `@media (min-width: 640px) { display: inline-block; }` | `sm:inline-block`          | Sets display to inline-block on small screens and up.|
|                             | `@media (min-width: 768px) { display: none; }`   | `md:hidden`                    | Hides element on medium screens and up.         |
| **Responsive Positioning**  | `position: static;`                             | `static`                        | Sets position to static for all screen sizes.   |
|                             | `@media (min-width: 640px) { position: relative; }` | `sm:relative`                | Sets position to relative on small screens and up.|
|                             | `@media (min-width: 768px) { position: absolute; }` | `md:absolute`                | Sets position to absolute on medium screens and up.|
| **Responsive Top**          | `top: 0;`                                        | `top-0`                         | Sets top to 0 for all screen sizes.             |
|                             | `@media (min-width: 640px) { top: 4px; }`        | `sm:top-1`                      | Sets top to 4px on small screens and up.        |
|                             | `@media (min-width: 768px) { top: 8px; }`        | `md:top-2`                      | Sets top to 8px on medium screens and up.       |
| **Responsive Right**        | `right: 0;`                                      | `right-0`                       | Sets right to 0 for all screen sizes.           |
|                             | `@media (min-width: 640px) { right: 4px; }`      | `sm:right-1`                   | Sets right to 4px on small screens and up.      |
|                             | `@media (min-width: 768px) { right: 8px; }`      | `md:right-2`                   | Sets right to 8px on medium screens and up.     |
| **Responsive Bottom**       | `bottom: 0;`                                     | `bottom-0`                      | Sets bottom to 0 for all screen sizes.          |
|                             | `@media (min-width: 640px) { bottom: 4px; }`     | `sm:bottom-1`                  | Sets bottom to 4px on small screens and up.     |
|                             | `@media (min-width: 768px) { bottom: 8px; }`     | `md:bottom-2`                  | Sets bottom to 8px on medium screens and up.    |
| **Responsive Left**         | `left: 0;`                                       | `left-0`                        | Sets left to 0 for all screen sizes.            |
|                             | `@media (min-width: 640px) { left: 4px; }`       | `sm:left-1`                     | Sets left to 4px on small screens and up.       |
|                             | `@media (min-width: 768px) { left: 8px; }`       | `md:left-2`                     | Sets left to 8px on medium screens and up.      |
