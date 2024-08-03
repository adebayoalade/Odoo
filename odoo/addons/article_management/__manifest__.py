{
    'name': 'Article Management',
    'version': '2.0',
    'summary': 'Manage articles assigned to readers',
    'description': 'This module allows managers to create articles, assign them to readers, and track their progress.',
    'author': 'David',
    'depends': ['base'],
    'data': [
        'security/article_security.xml',
        'security/ir.model.access.csv',
        'views/article_views.xml',
        'views/article_templates.xml',
        'report/article_report.xml',
    ],
    'demo': [
        'demo/article_demo.xml',
    ],
    'test': [
        'tests/test_article.py',
    ],
}
