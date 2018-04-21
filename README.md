# concept-negotiation## Prototype Concept Negotiation Using Conceptual Spaces

**Under Construction**

In this project we consider how Conceptual Spaces can be used for concept negotiation.

This is based on the work of Lucas Bechberger et al. (https://github.com/lbechberger/ConceptualSpaces) providing an implementation of Conceptual Spaces (see Lucas Bechberger and Kai-Uwe Kühnberger. "A Thorough Formalization of Conceptual Spaces". 40th German Conference on Artificial Intelligence, 2017).

### Getting Started
This code is based on https://github.com/lbechberger/ConceptualSpaces and requires this repository to run.
#### Concept Updating
The snippets of code provide a simple method for updating concepts with new information as well as a function to calculate the geometric centre of concepts in order to represent prototypes. The code is made to work when appended to https://github.com/lbechberger/ConceptualSpaces/blob/master/conceptual_spaces/demo/fruit_space.py

As an example, fruit_space.png shows a conceptual space representing various fruits (again, from https://github.com/lbechberger/ConceptualSpaces/blob/master/conceptual_spaces/demo/fruit_space.py). fruit_spaces_updated_pear.png shows the conceptual space after being updated with `updateconcept(pear,[0.25,0.5,0.65])`.
