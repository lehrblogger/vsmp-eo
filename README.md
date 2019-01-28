# Use your Electric Objects hardware as a Very Slow Movie Player

[Bryan Boyer](https://twitter.com/bryanboyer) created a wondrous object that he called a [Very Slow Movie Player](https://medium.com/s/story/very-slow-movie-player-499f76c48b62). It uses an ePaper display to play a movie at 24 frames per _hour_.

> Slowing things down to an extreme measure creates room for appreciation of the object, but the prolonged duration shifts the relationship between object, viewer, and context. A film watched at 1/3,600 of the original speed is not merely a very slow movie, it’s a hazy timepiece. And while a thing like _Very Slow Movie Player (VSMP)_ wouldn’t tell you the time, it helps you see yourself against the smear of time.

I had been looking for new content for my [Electric Objects](https://www.electricobjects.com/) [EO1](https://www.kickstarter.com/projects/electricobjects/electric-objects-a-computer-made-for-art), so decided to turn it into a VSMP. The backlit, full-color EO1 hardware creates a very different experience than ePaper, so I'd have to forgo the beautiful interactions with ambient light, but I couldn't bear to watch the [_2001_](https://www.imdb.com/title/tt0062622/) ["Star Gate" sequence](https://www.google.com/search?tbm=isch&q=2001+star+gate) in black-and-white...

Want to do this yourself?

 1. You can use https://www.electricobjects.com/set_url to show an arbitrary URL on your device.
 2. You'll need to first extract the frames from whatever movie file you'd like to play slowly. [FFmpeg](https://www.ffmpeg.org/) is great for this. As an alternative, I considered playing the movie file one frame at a time in the browser, but wasn't sure my EO1 would be up to the task and was less familiar with the Javascript involved.
 3. You'll need to host the frames, along with the index page, somewhere your device can see them. A two-hour movie could easily have a few hundred GBs worth of 1920x1080 frames, so you'll probably want to do this from a machine running a web server on your local wi-fi network.
 4. There are a few URL parameters for specifying the frame rate (e.g. 30 or 60fps), whether you want to crop or letterbox the frames onto your 16:9 device, and the frame number at which you'd like to start. That last one is useful if you need to pause and want to pick up where you left off, and is why the current frame number is displayed in the top-left corner.
 2. The included mounting hardware works well in landscape, but the browser won't know that it's sideways, so the CSS uses `transform: rotate` accordingly.

Let me know if you have any questions!
