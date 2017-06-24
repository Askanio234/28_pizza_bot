Пицца из нашего меню:

{% for entry in catalog -%}
*{{ entry.title }} #{{loop.index}}*
{{ entry.description }}
    {{ entry.first_option.size }} - *{{ entry.first_option.price }} руб.*
    {{ entry.second_option.size }} - *{{ entry.second_option.price }} руб.*

{% endfor %}
