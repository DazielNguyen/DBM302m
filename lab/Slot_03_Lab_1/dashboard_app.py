"""
Sales Dashboard Application
Professional interactive dashboard for sales data analysis
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ============================================================================
# DATA LOADING AND PREPROCESSING
# ============================================================================

try:
    # Load sales data from CSV file
    df = pd.read_csv('sales_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    print("Đã tải dữ liệu thành công từ sales_data.csv")
except FileNotFoundError:
    print("Cảnh báo: Không tìm thấy sales_data.csv. Sử dụng dữ liệu mẫu để minh họa.")
    # Create mock data for demonstration
    df = pd.DataFrame({
        'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'] * 20,
        'Amount': [1000, 500, 300, 400, 100] * 20,
        'Date': pd.date_range('2024-01-01', periods=100, freq='D'),
        'Region': ['North', 'South', 'East', 'West', 'Central'] * 20,
        'Quantity': [5, 10, 8, 3, 15] * 20
    })

# ============================================================================
# DASH APP INITIALIZATION
# ============================================================================

app = dash.Dash(__name__)
app.title = "Bảng Điều Khiển Phân Tích Doanh Số"

# ============================================================================
# LAYOUT DESIGN
# ============================================================================

app.layout = html.Div([
    # Header Section
    html.Div([
        html.H1("Bảng Điều Khiển Phân Tích Doanh Số", 
                style={
                    'textAlign': 'center', 
                    'color': '#1a1a1a',
                    'fontFamily': 'Arial, sans-serif',
                    'fontWeight': '600',
                    'marginBottom': '10px',
                    'fontSize': '32px'
                }),
        html.P("Trực quan hóa dữ liệu tương tác và phân tích kinh doanh thông minh",
               style={
                   'textAlign': 'center',
                   'color': '#666',
                   'fontFamily': 'Arial, sans-serif',
                   'fontSize': '14px',
                   'marginTop': '0'
               })
    ], style={
        'backgroundColor': '#f8f9fa',
        'padding': '20px',
        'borderBottom': '3px solid #007bff',
        'marginBottom': '30px'
    }),
    
    # Instructions Section
    html.Div([
        html.P("Hướng dẫn: Nhấp và kéo để chọn sản phẩm trên biểu đồ cột. Biểu đồ đường sẽ tự động cập nhật xu hướng của sản phẩm được chọn.",
               style={
                   'textAlign': 'center',
                   'color': '#495057',
                   'fontFamily': 'Arial, sans-serif',
                   'fontSize': '13px',
                   'fontStyle': 'italic',
                   'marginBottom': '20px'
               })
    ]),
    
    # Charts Container
    html.Div([
        # Bar Chart Section
        html.Div([
            html.Div([
                html.H3("Phân Tích Hiệu Suất Sản Phẩm",
                        style={
                            'color': '#2c3e50',
                            'fontFamily': 'Arial, sans-serif',
                            'fontSize': '18px',
                            'fontWeight': '600',
                            'marginBottom': '15px',
                            'borderBottom': '2px solid #e9ecef',
                            'paddingBottom': '10px'
                        }),
                dcc.Graph(id='bar-chart', 
                          config={
                              'displayModeBar': True, 
                              'displaylogo': False,
                              'staticPlot': False,
                              'doubleClick': 'reset',
                              'scrollZoom': True
                          },
                          style={'height': '500px'})
            ], style={
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'height': '100%'
            })
        ], style={'width': '48%'}),
        
        # Line Chart Section
        html.Div([
            html.Div([
                html.H3("Phân Tích Xu Hướng Doanh Số",
                        style={
                            'color': '#2c3e50',
                            'fontFamily': 'Arial, sans-serif',
                            'fontSize': '18px',
                            'fontWeight': '600',
                            'marginBottom': '15px',
                            'borderBottom': '2px solid #e9ecef',
                            'paddingBottom': '10px'
                        }),
                dcc.Graph(id='line-chart',
                          config={
                              'displayModeBar': True, 
                              'displaylogo': False,
                              'staticPlot': False,
                              'doubleClick': 'reset',
                              'scrollZoom': True
                          },
                          style={'height': '500px'})
            ], style={
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'height': '100%'
            })
        ], style={'width': '48%'})
    ], style={
        'display': 'flex', 
        'justifyContent': 'space-between',
        'padding': '0 20px',
        'gap': '20px'
    }),
    
    # Footer Section
    html.Div([
        html.P("Bảng điều khiển được xây dựng bằng Dash & Plotly | Nền tảng Phân Tích Dữ Liệu",
               style={
                   'textAlign': 'center',
                   'color': '#999',
                   'fontFamily': 'Arial, sans-serif',
                   'fontSize': '12px',
                   'marginTop': '40px',
                   'paddingTop': '20px',
                   'borderTop': '1px solid #e9ecef'
               })
    ])
], style={
    'backgroundColor': '#f5f5f5',
    'minHeight': '100vh',
    'paddingBottom': '30px',
    'fontFamily': 'Arial, sans-serif'
})

# ============================================================================
# CALLBACK FUNCTIONS - INTERACTIVE LOGIC
# ============================================================================

@app.callback(
    [Output('bar-chart', 'figure'),
     Output('line-chart', 'figure')],
    [Input('bar-chart', 'selectedData')]
)
def update_charts(selectedData):
    """
    Update both charts based on user selection
    
    Args:
        selectedData: Data points selected by user on bar chart
        
    Returns:
        tuple: (bar_figure, line_figure)
    """
    
    # Filter data based on selection
    if selectedData is None or not selectedData.get('points'):
        # No selection - show all data
        filtered_df = df
        title_suffix = " (Tất Cả Sản Phẩm)"
    else:
        # Get selected products
        selected_products = [point['x'] for point in selectedData['points']]
        filtered_df = df[df['Product'].isin(selected_products)]
        title_suffix = f" ({len(selected_products)} Đã Chọn)"
    
    # ========================================================================
    # BAR CHART: Total Sales by Product
    # ========================================================================
    product_sales = filtered_df.groupby('Product')['Amount'].sum().reset_index()
    product_sales = product_sales.sort_values('Amount', ascending=False)
    
    bar_fig = px.bar(
        product_sales, 
        x='Product', 
        y='Amount',
        title=f'Tổng Doanh Số Theo Sản Phẩm{title_suffix}',
        color='Amount',
        color_continuous_scale='Blues',
        labels={'Amount': 'Tổng Doanh Số (VNĐ)', 'Product': 'Tên Sản Phẩm'}
    )
    
    bar_fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Arial, sans-serif', size=12, color='#333'),
        title=dict(font=dict(size=16, color='#2c3e50'), x=0.5, xanchor='center'),
        xaxis=dict(showgrid=False, showline=True, linewidth=1, linecolor='#ddd'),
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='#f0f0f0'),
        dragmode='select',
        hovermode='closest',
        uirevision='bar-chart-constant',
        autosize=True,
        transition={'duration': 0}
    )
    
    bar_fig.update_traces(
        hovertemplate='<b>%{x}</b><br>Doanh số: %{y:,.0f} VNĐ<extra></extra>'
    )
    
    # ========================================================================
    # LINE CHART: Sales Trend Over Time
    # ========================================================================
    daily_sales = filtered_df.groupby('Date')['Amount'].sum().reset_index()
    daily_sales = daily_sales.sort_values('Date')
    
    # Calculate fixed date range from original data to prevent auto-scaling
    date_min = df['Date'].min()
    date_max = df['Date'].max()
    
    line_fig = px.line(
        daily_sales, 
        x='Date', 
        y='Amount',
        title=f'Xu Hướng Doanh Số Theo Thời Gian{title_suffix}',
        markers=True,
        labels={'Amount': 'Doanh Số Hàng Ngày (VNĐ)', 'Date': 'Ngày Tháng'}
    )
    
    line_fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Arial, sans-serif', size=12, color='#333'),
        title=dict(font=dict(size=16, color='#2c3e50'), x=0.5, xanchor='center'),
        xaxis=dict(
            showgrid=True, 
            gridwidth=1, 
            gridcolor='#f0f0f0',
            range=[date_min, date_max],
            fixedrange=False,
            autorange=False
        ),
        yaxis=dict(
            showgrid=True, 
            gridwidth=1, 
            gridcolor='#f0f0f0',
            fixedrange=False,
            autorange=True
        ),
        hovermode='x unified',
        uirevision='line-chart-constant',
        autosize=True,
        transition={'duration': 0},
        updatemenus=[]
    )
    
    line_fig.update_traces(
        line=dict(color='#007bff', width=2.5),
        marker=dict(size=6, color='#0056b3', line=dict(width=1, color='white')),
        hovertemplate='Ngày: %{x|%Y-%m-%d}<br>Doanh số: %{y:,.0f} VNĐ<extra></extra>'
    )
    
    return bar_fig, line_fig

# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Đang khởi động Bảng Điều Khiển Phân Tích Doanh Số...")
    print("="*60)
    print("URL Dashboard: http://127.0.0.1:8050")
    print("Nhấn CTRL+C để dừng server")
    print("="*60 + "\n")
    
    app.run(debug=True, port=8050)
