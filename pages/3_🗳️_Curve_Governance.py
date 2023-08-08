# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image
from subgrounds import Subgrounds
from subgrounds import SyntheticField

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='Curve Governance Functionality During Hack Attack - DeFi In Danger',
                   page_icon=':bar_chart:🔥', layout='wide')
st.title('🔥 Curve Governance Functionality During Hack Attack')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#########################################################################################
####################################### Data Sources ####################################

# Instantiate the subgrounds object
sg = Subgrounds()


# Load curve dao Subgraph
curve_dao_subgraph = sg.load_subgraph(
    "https://api.thegraph.com/subgraphs/name/convex-community/curve-dao"
)

# Query proposals from curve dao subgraph
proposal_curve = curve_dao_subgraph.Query.proposals(
    first=1000,
    orderBy=curve_dao_subgraph.Proposal.startDate,
    orderDirection="desc",
)


# Convert Date Count to user friendly human readable format using SyntheticField
curve_dao_subgraph.Proposal.datetime = SyntheticField.datetime_of_timestamp(
    curve_dao_subgraph.Proposal.startDate)


# Calculate voting ratio
curve_dao_subgraph.Proposal.voting_ratio = (curve_dao_subgraph.Proposal.votesFor) / (
    curve_dao_subgraph.Proposal.votesAgainst + curve_dao_subgraph.Proposal.votesFor)


# Voting for and against power rescale
curve_dao_subgraph.Proposal.votesFor_rescale = curve_dao_subgraph.Proposal.votesFor / 10 ** 18
curve_dao_subgraph.Proposal.votesAgainst_rescale = curve_dao_subgraph.Proposal.votesAgainst / 10 ** 18

# Voting support required
curve_dao_subgraph.Proposal.req_supp_percent = curve_dao_subgraph.Proposal.supportRequired / 10 ** 18


# Voting Participation Rate
curve_dao_subgraph.Proposal.participation_rate = (
    curve_dao_subgraph.Proposal.votesAgainst + curve_dao_subgraph.Proposal.votesFor) / (curve_dao_subgraph.Proposal.totalSupply)

# Min Required quorum percentage
curve_dao_subgraph.Proposal.req_quorum_percent = curve_dao_subgraph.Proposal.minAcceptQuorum / 10 ** 18

# Proposal Total Supply rescale
curve_dao_subgraph.Proposal.totalSupply_rescale = curve_dao_subgraph.Proposal.totalSupply / 10 ** 18


# Make data Frame out of query

df = sg.query_df(
    [
        proposal_curve.id,
        proposal_curve.datetime,

        proposal_curve.voteCount,
        proposal_curve.votesFor_rescale,
        proposal_curve.votesAgainst_rescale,
        proposal_curve.voting_ratio,
        proposal_curve.req_supp_percent,
        proposal_curve.participation_rate,
        proposal_curve.req_quorum_percent,


        proposal_curve.metadata,
        proposal_curve.creator,
        proposal_curve.totalSupply_rescale,

    ]
)

df1 = df.head(10)
df2 = df1[['proposals_datetime',
           'proposals_voteCount', 'proposals_voting_ratio', 'proposals_participation_rate', 'proposals_req_supp_percent', 'proposals_metadata']]

df3 = df.sort_values(['proposals_participation_rate'],
                     ascending=False).head(10)

#################################################################################################
######################################### Visualization #########################################


st.write(""" ### How Curve Finance Governance Works  ? ##  """)

st.write("""
The governance of Curve Finance is managed through a decentralized autonomous organization (DAO) structure, which allows token holders to participate in decision-making processes related to the protocol's development, upgrades, and parameters. **CRV Token**: Curve's native governance token is called CRV. CRV token holders have the right to participate in governance decisions by voting on proposals. The number of votes a holder has is proportional to the number of CRV tokens they own.    
**Governance Proposals**: Anyone in the community can create a governance proposal. These proposals can cover a wide range of topics, such as protocol upgrades, changes to trading fees, parameter adjustments, partnerships, and more. Once a proposal is created, it goes through a voting process. CRV token holders can vote either in favor, against, or abstain from a proposal. The voting period typically lasts for a specific number of days. For a proposal to be considered valid, it often needs to meet certain quorum and approval thresholds. Quorum refers to the minimum percentage of total CRV tokens that need to be participating in the vote. Approval thresholds determine the minimum percentage of votes needed to pass a proposal.If a proposal reaches the required quorum and approval thresholds, and the voting period concludes, the proposal can be executed based on the outcome. The specific execution process might vary depending on the protocol's technical implementation.
""")


st.info(""" ##### In This Curve Finance Governance Section you can find: ####

* Market Over view [2 Month Period]
* Blend Impact on Blur Platform  [2 Month Period]





""")


#################################################################################################
# Daily Numner of Distinct Borrower
fig = px.bar(df.head(100), x='proposals_id', y="proposals_voteCount", color='proposals_datetime',
             title='Daily Numner of Distinct Borrower')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Distinct Number of Borrower')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df2)
