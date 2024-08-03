{
    'name': 'Article Management',
    'version': '2.0',
    'summary': 'Manage articles assigned to readers',
    'description': 'This module allows managers to create articles, assign them to readers, and track their progress.',
    'author': 'David',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/article_views.xml',
        'views/article_menu.xml',
        # 'views/article_filter.xml',
        'report/article_report.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'test': [
        'tests/test_article.py',
    ],
}
