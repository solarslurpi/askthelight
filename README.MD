# Welcome to Ask The Light!

If you wish to contact me: @happyday@mastodon.world Thank you. I would very much like to hear from you. To hear your thoughts. Particularly those that can improve this project (and hence my own knowledge).

# What

This project presents a one page web site where a person can enter a word or phrase they are curious what Jesus thought about and then openai ChapGPT will respond with what Jesus would think about the topic. For example, I entered the topic `men versus women` and the response was:

```
Jesus would have thought that men and women are equal in the eyes of God. This is evidenced in the New Testament, where Jesus speaks of the importance of treating all people with respect and dignity. In Matthew 22:39, Jesus says, “You shall love your neighbor as yourself.” This passage shows that Jesus believed that all people should be treated with love and respect, regardless of gender. In Galatians 3:28, Paul writes, “There is neither Jew nor Greek, there is neither slave nor free, there is no male and female, for you are all one in Christ Jesus.” This passage shows that Jesus believed that all people, regardless of gender, were equal in the eyes of God. Finally, in Luke 10:27, Jesus says, “You shall love the Lord your God with all your heart and with all your soul and with all your strength and with all your mind, and your neighbor as yourself.” This passage shows that Jesus believed that all people should be treated with love and respect, regardless of gender.
```

And the next time I entered the phrase, I'd get a different response with different Bible passages. Wonderful. And the good news is, the more I test, the more I know about Jesus and the Bible!

# Meet My New

No two people can have the same context, but what if n people chime in on and agree on a perspective Jesus would have on a topic? And to my amazement - ChatGPT interviewed for the position. I was very excited. Here was a big-hair-o-software that was not woman, man, animal, or insect. It is AI. I look at AI as offering the potential to provide a unique perspective that synthesizes information from diverse sources, avoiding the limitations of individual biases or agendas.

After interviewing ChatGPT and giving it a job, in it's excitement ChatGPT responded with:

```
I appreciate your perspective on using AI to gain a well-rounded understanding of Jesus' thoughts on a topic. As an AI language model, I have been trained on a vast array of text data, including religious texts, scholarly articles, and various interpretations of Jesus' teachings. My purpose is to provide unbiased, informative responses that draw from this collective knowledge.
```

OK ChatGPT. I'm hoping you're right and not blowing smoke. Time will tell.

## Goals

The goals of this project include:

- Build a one page web site where a person (...or perhaps a cat. I have noticed some cats can type?) enters a topic they want Jesus' thoughts on. ChatGPT provides an answer.
- Evolve my knowledge of using generative text APIs. When a powerful technology in born, I want to grasp (perhaps never completely understanding) it's power for good (and evil)

### Example

For example, back to the phrased discussed earlier, "men versus women".

```
#### Prompt 1 got this result:

You asked about men versus women. The topic Jesus will address is men versus women. The reason for this is The topic is non-offensive, non-trivial, spelled correctly, and comprehensible, so the meaningful topic is the same as the original topic.

What did Jesus think about men versus women

#### Prompt 2 got this result:
Jesus would have thought that men and women are equal in the eyes of God. This is evidenced in the New Testament, where Jesus speaks of the importance of treating all people with respect and dignity. In Matthew 22:39, Jesus says, “You shall love your neighbor as yourself.” This passage shows that Jesus believed that all people should be treated with love and respect, regardless of gender. In Galatians 3:28, Paul writes, “There is neither Jew nor Greek, there is neither slave nor free, there is no male and female, for you are all one in Christ Jesus.” This passage shows that Jesus believed that all people, regardless of gender, were equal in the eyes of God. Finally, in Luke 10:27, Jesus says, “You shall love the Lord your God with all your heart and with all your soul and with all your strength and with all your mind, and your neighbor as yourself.” This passage shows that Jesus believed that all people should be treated with love and respect, regardless of gender.

Jesus believed that men and women should be treated equally and with respect. He taught that all people should be treated with love and respect, regardless of gender. He also taught that all people, regardless of gender, were equal in the eyes of God. Jesus' teachings on this topic are clear and consistent throughout the New Testament. He believed that men and women should be treated with respect and dignity, and that all people should be treated with love and kindness.

```

To get to the response, the topic ("men versus women")

- first stops off in the [`moderator.py`](https://github.com/solarslurpi/askthelight/blob/main/moderator.py) to check if the content should be flagged based on openai's Moderation API.
- if openai's API determined the topic is not offensive, it calls into the `jesus_thoughts()` function found in [`ask_the_light.py`](https://github.com/solarslurpi/askthelight/blob/main/ask_the_light.py). For getting the best results, I found chaining two prompts together worked best.
  - The first prompt's job is to make sure the topic is meaningful to Jesus to address. I spent days fascinated by openai's responses. You'll notice in the text where openai tells us what the meaningful topic is that it gave it's reason for the topic choice. This helped me understand what was the most influential text in the prompt that determined that particular topic. The first prompt is in [`prompt_topic.txt](https://github.com/solarslurpi/askthelight/blob/main/prompts/Jesus/prompt_topic.txt).
  - The second prompt's job is to write out Jesus' thoughts as interpreted by openai. The second prompt is in [`prompt_response.txt`](https://github.com/solarslurpi/askthelight/blob/main/prompts/Jesus/prompt_response.txt)
- `jesus_thoughts()` makes the two calls to the openai completion API and returns the message.

I'm interested in how the web page responds when others use it. That is the step I am at right now.
